from django.db import models

class User(models.Model):
    class Meta(object):
        db_table = 'user'

    name = models.CharField(
        'Name', blank=False, null=False, db_index=True, max_length=50
    )

    email = models.EmailField(
        'Email', blank=False, null=False, db_index=True, max_length=100
    )

    password = models.CharField(
        'Password', blank=False, null=False, db_index=True, max_length=100, 
    )

    token = models.CharField(
        'Token', blank=True, null=True, db_index=True, max_length=100
    )

    token_expires_at = models.DateTimeField(
        'Token Expires At', blank=True
    )

    created_at = models.DateTimeField(
        'Created At', blank=True , auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )