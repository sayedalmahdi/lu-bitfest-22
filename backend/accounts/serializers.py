from .models import User, Official
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class OfficialRegisterSerializer(RegisterSerializer):
    official = serializers.PrimaryKeyRelatedField(read_only=True)
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
        fields = ('username', 'name', 'contact_number', 'usertype')

class UserSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='official.name')
    contact_number = serializers.ReadOnlyField(source='official.contact_number')

    class Meta:
        model = User
        fields = ('username', 'usertype', 'name', 'contact_number')