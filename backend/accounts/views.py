from django.shortcuts import render
from .models import User, Official
from dj_rest_auth.registration.views import RegisterView
from accounts.serializers import OfficialSerializer, OfficialRegisterSerializer, UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class OfficialRegisterView(RegisterView):
    serializer_class = OfficialRegisterSerializer

class ListOfficialView(generics.ListAPIView):
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer

class OfficialDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        official = Official.objects.get(official=request.user)
        serializer = OfficialSerializer(official)
        return Response(serializer.data)

class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        usertype = user.usertype

        # now get object of the user type
        if usertype == 'official':
            official = Official.objects.get(official=user)
            serializer = OfficialSerializer(official)

        return Response(serializer.data)