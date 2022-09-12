from django.shortcuts import render
from .models import BusInventory, Stoppage, Route
from .serializers import BusInventorySerializer, StoppageSerializer, RouteSerializer
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

class StoppageListCreate(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Stoppage.objects.all()
    serializer_class = StoppageSerializer

class StoppageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Stoppage.objects.all()
    serializer_class = StoppageSerializer

class RouteListCreate(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Route.objects.all()
    serializer_class = RouteSerializer