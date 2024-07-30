from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Category
from config.constants import PRODUCT_TYPE
# Create your models here.


class Product(models.Model):
    class Meta:
        db_table='Product'

    name = models.CharField(
        'Name',blank=False,null=False,max_length=50,db_index=True
    )

    description=models.TextField(
        'Description',blank=True,null=True,max_length=500,db_index=True
    )

    price = models.FloatField(
        'Price', blank=False , null = False
    )

    image = CloudinaryField(
        'Image', blank=True , null = True
    )

    type = models.CharField(
        'Type',blank=False,null=False,max_length=30,choices=PRODUCT_TYPE
    )

    category = models.ForeignKey(
     Category,related_name='related_category',on_delete=models.CASCADE
    )
