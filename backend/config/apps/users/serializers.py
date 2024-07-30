from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import check_password,make_password
from secrets import token_hex
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','token','token_expires_at')


class UserSignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only = True , required = True)
    token = serializers.CharField(read_only = True)
    token_expires_at = serializers.DateTimeField(read_only = True)

    class Meta:
        model = User
        fields = ('id','name','email','password','token','token_expires_at')

    def create(self, validated_data):
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'email':['This email is already taken']})
        
        validated_data['password'] = make_password(validated_data['password'])

        validated_data['token'] = token_hex(16)
        validated_data['token_expires_at'] = datetime.datetime.now() + datetime.timedelta(days=7)

        return super().create(validated_data)
    

class UserSignInSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only = True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only =True)
    token = serializers.CharField(read_only = True) 
    token_expires_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('id','name','email','password','token','token_expires_at')

    def create(self, validated_data):

        user = User.objects.filter(email = validated_data['email'])

        if len(user) > 0 and check_password(validated_data['password'],user[0].password):
            user[0].token = token_hex(16)
            user[0].token_expires_at = datetime.datetime.now() + datetime.timedelta(days=7)
            user[0].save()

            return user[0]
        else:
            raise serializers.ValidationError({'error':['The password or email is incorrect']})


