from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import ProjectPair

class PPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPair
        fields = '__all__'