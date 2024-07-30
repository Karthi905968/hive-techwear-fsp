from rest_framework import generics
from .models import Product
from apps.users.mixins import CustomLoginRequiredMixin
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

class ProductList(CustomLoginRequiredMixin,generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [ DjangoFilterBackend , filters.SearchFilter ]
    filterset_fields = ['category_id','type']
    search_fileds = ['name','description']