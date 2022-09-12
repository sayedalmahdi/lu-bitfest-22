from django.shortcuts import render
from .models import BusInventory
from .serializers import BusInventorySerializer
from rest_framework import generics
from rest_framework import permissions

from accounts.permissions import IsOfficialOrReadOnly

class BusInventoryListCreate(generics.ListCreateAPIView):
    permission_classes = []
    queryset = BusInventory.objects.all()
    serializer_class = BusInventorySerializer

class BusInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = BusInventory.objects.all()
    serializer_class = BusInventorySerializer