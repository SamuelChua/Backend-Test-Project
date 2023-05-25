from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.conf import settings
from .models import ProjectPair

class PPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPair
        fields = '__all__'


    

