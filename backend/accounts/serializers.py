from .models import User, Official, Student, Teacher, Staff
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class OfficialRegisterSerializer(RegisterSerializer):
    official = serializers.RelatedField(many=False, read_only=True)
    name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'contact_number', 'official')
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        data = super(OfficialRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
            'contact_number': self.validated_data.get('contact_number', '')
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(OfficialRegisterSerializer, self).save(request)
        user.usertype = 'official'
        user.save()
        official = Official.objects.create(official=user, name=self.validated_data.get('name', ''), contact_number=self.validated_data.get('contact_number', ''))
        official.save()
        return user

class OfficialSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='official.username')
    usertype = serializers.ReadOnlyField(source='official.usertype')
    
    class Meta:
        model = Official
        fields = ('id', 'username', 'name', 'contact_number', 'usertype')

class StudentRegisterSerializer(RegisterSerializer):
    student = serializers.RelatedField(many=False, read_only=True)
    name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'contact_number', 'student')
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        data = super(StudentRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
            'contact_number': self.validated_data.get('contact_number', ''),
            'batch_number': self.validated_data.get('batch_number', ''),
            'section': self.validated_data.get('section', '')
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(StudentRegisterSerializer, self).save(request)
        user.usertype = 'student'
        user.save()
        student = Student.objects.create(student=user, name=self.validated_data.get('name', ''), contact_number=self.validated_data.get('contact_number', ''), batch_number=self.validated_data.get('batch_number', ''), section=self.validated_data.get('section', ''))
        student.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='student.username')
    usertype = serializers.ReadOnlyField(source='student.usertype')
    
    class Meta:
        model = Student
        fields = ('id', 'username', 'name', 'contact_number', 'batch_number', 'section', 'usertype')

class TeacherRegisterSerializer(RegisterSerializer):
    teacher = serializers.RelatedField(many=False, read_only=True)
    name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    codename = serializers.CharField(max_length=100)
    designation = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'contact_number', 'teacher')
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        data = super(TeacherRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
            'contact_number': self.validated_data.get('contact_number', ''),
            'department': self.validated_data.get('department', ''),
            'codename': self.validated_data.get('codename', ''),
            'designation': self.validated_data.get('designation', '')
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(TeacherRegisterSerializer, self).save(request)
        user.usertype = 'teacher'
        user.save()
        teacher = Teacher.objects.create(teacher=user, name=self.validated_data.get('name', ''), contact_number=self.validated_data.get('contact_number', ''), department=self.validated_data.get('department', ''), codename=self.validated_data.get('codename', ''), designation=self.validated_data.get('designation', ''))
        teacher.save()
        return user

class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='teacher.username')
    usertype = serializers.ReadOnlyField(source='teacher.usertype')
    
    class Meta:
        model = Teacher
        fields = ('id', 'username', 'name', 'contact_number', 'department', 'codename', 'designation', 'usertype')

class StaffRegisterSerializer(RegisterSerializer):
    staff = serializers.RelatedField(many=False, read_only=True)
    name = serializers.CharField(max_length=100)
    contact_number = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'contact_number', 'staff')
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        data = super(StaffRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'name': self.validated_data.get('name', ''),
            'contact_number': self.validated_data.get('contact_number', '')
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(StaffRegisterSerializer, self).save(request)
        user.usertype = 'staff'
        user.save()
        staff = Staff.objects.create(staff=user, name=self.validated_data.get('name', ''), contact_number=self.validated_data.get('contact_number', ''))
        staff.save()
        return user

class StaffSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='staff.username')
    usertype = serializers.ReadOnlyField(source='staff.usertype')
    
    class Meta:
        model = Staff
        fields = ('id', 'username', 'name', 'contact_number', 'usertype')

class UserSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='official.name')
    contact_number = serializers.ReadOnlyField(source='official.contact_number')

    class Meta:
        model = User
        fields = ('id', 'username', 'usertype', 'name', 'contact_number')