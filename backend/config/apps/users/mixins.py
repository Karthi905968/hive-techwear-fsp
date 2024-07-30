from rest_framework import status
from django.utils import timezone
from django.http import JsonResponse
from .models import User
from config.helpers.error_response import error_response

class CustomLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return error_response('Please set Auth-Token', status.HTTP_401_UNAUTHORIZED)

        token = request.headers['Authorization']
        now = timezone.now()

        try:
            login_user = User.objects.get(token=token, token_expires_at__gt=now)
        except User.DoesNotExist:
            return error_response('The token is invalid or expired', status.HTTP_401_UNAUTHORIZED)

        request.login_user = login_user
        return super().dispatch(request, *args, **kwargs)
