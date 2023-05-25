from rest_framework import generics  # <- import generics
from .models import ProjectPair  # <- don't forget your models
from .serializers import PPSerializer

class PPViewSet(generics.ListCreateAPIView):
    queryset = ProjectPair.objects.all()
    serializer_class = PPSerializer
