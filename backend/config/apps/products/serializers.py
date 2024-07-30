from rest_framework import serializers
from .models import Product
from apps.categories.serializers import CategorySerializer
from rest_framework.fields import ImageField

class ProductSerializer(serializers.ModelSerializer):   
    image = ImageField(read_only = True)
    category = CategorySerializer(many = False , read_only = True)

    class Meta:
        model = Product
        fields = '__all__'
        depath = 1


