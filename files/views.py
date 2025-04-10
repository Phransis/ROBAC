from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import File, Folder
from .serializers import FileSerializer, FolderSerializer
from rest_framework.response import Response

# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role not in ['super_admin', 'super_admin_maker', 'super_admin_checker']:
            return Response({'error': 'You do not have permission to create files.'}, status=403)
        # Custom logic before creating the file
        return super().create(request, *args, **kwargs)
    
class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role not in ['super_admin', 'super_admin_maker', 'super_admin_checker']:
            return Response({'error': 'You do not have permission to create folders.'}, status=403)
        # Custom logic before creating the folder
        return super().create(request, *args, **kwargs)