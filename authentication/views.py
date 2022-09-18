from django.shortcuts import render
from .serializers import ObtainTokenSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
from rest_framework import generics

# Create your views here.

class obtainTokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serliazer_class = ObtainTokenSerializer

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer
    