from django.shortcuts import render
from .models import User, Official, Student, Teacher, Staff
from dj_rest_auth.registration.views import RegisterView
from accounts.serializers import OfficialSerializer, OfficialRegisterSerializer, StudentRegisterSerializer, StudentSerializer, TeacherRegisterSerializer, TeacherSerializer, StaffRegisterSerializer, StaffSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOfficialOrReadOnly, IsOfficial, IsStudent, IsTeacher, IsStaff

class OfficialRegisterView(RegisterView):
    serializer_class = OfficialRegisterSerializer

class StudentRegisterView(RegisterView):
    serializer_class = StudentRegisterSerializer

class TeacherRegisterView(RegisterView):
    serializer_class = TeacherRegisterSerializer

class StaffRegisterView(RegisterView):
    serializer_class = StaffRegisterSerializer

class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        usertype = user.usertype

        # now get object of the user type
        if usertype == 'official':
            official = Official.objects.get(official=user)
            serializer = OfficialSerializer(official)

        return Response(serializer.data)

class OfficialListView(generics.ListAPIView):
    permission_classes = []
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer

class StudentListView(generics.ListAPIView):
    permission_classes = []
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherListView(generics.ListAPIView):
    permission_classes = []
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StaffListView(generics.ListAPIView):
    permission_classes = []
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class OfficialDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer

class StudentDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StaffDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer