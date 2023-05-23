from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ProjectPair

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add other fields as needed

class ProjectPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPair
        fields = ['user', 'email']  # Add other fields as needed
