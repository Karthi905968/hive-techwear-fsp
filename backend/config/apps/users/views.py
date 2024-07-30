from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.users.mixins import CustomLoginRequiredMixin
from .models import User
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer

class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer

class UserProfile(CustomLoginRequiredMixin, generics.ListAPIView):
    serializer_class=UserSerializer
    pagination_class=None

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer([request.login_user],many=True)
        return Response(serializer.data[0])
   

        