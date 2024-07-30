from django.urls import path
from .views import UserSignUp,UserSignIn,UserProfile

urlpatterns = [
    path('signup/',UserSignUp.as_view(),name='sign-up'),
    path('signin/',UserSignIn.as_view(),name='sign-in'),
    path('profile/',UserProfile.as_view(),name='profile'),
]

