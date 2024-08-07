from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

