from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'Category'

    name = models.CharField(
        'Name',max_length=50,blank=False,null=False,db_index=True
    )
    
    image = CloudinaryField(
        'Image', blank = False , null = False
    )

    created_at = models.DateTimeField(
        'Created Date', blank=True , auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated Date', blank=True , auto_now=True
    )

