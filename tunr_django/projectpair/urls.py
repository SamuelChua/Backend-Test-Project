from django.urls import path, include
from .views import PPViewSet

urlpatterns = [
  path('', PPViewSet.as_view(), name='projectpair'),
]