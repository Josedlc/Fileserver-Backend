from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.views import verify_token
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.

from .serializers import FileSerializer, DepartmentSerializer, FileUpSerializer
from .models import File, Department

class DepartmentViewSet(ModelViewSet):
    queryset= Department.objects.all()
    serializer_class = DepartmentSerializer


class FileViewSet(ModelViewSet):
    queryset= File.objects.all()
    serializer_class = FileSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class FileUpViewSet(ModelViewSet):
    queryset= File.objects.all()
    serializer_class = FileUpSerializer



class FileView(APIView):
    def get(self, request):
        payload = verify_token(request)
        file = File.objects.all()
        serializer = FileSerializer(file, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pass

    def delete(self,request):
        file.is_active = False
        file.save()
        return Response(data='delete success')
      

    def put(self,request):
        pass

    def patch(self,request):
        pass