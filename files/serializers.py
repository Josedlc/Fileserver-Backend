from rest_framework import serializers
from django.utils.text import gettext_lazy as _
from .models import File, Department
from users.serializers import UserNameSerializer

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class FileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = File
        fields = ('id', 'title', 'date', 'user', 'department', 'file_save')

class FileUpSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    department = DepartmentSerializer()
    class Meta: 
        model = File
        fields = ('id', 'title', 'date', 'user', 'department', 'file_save')