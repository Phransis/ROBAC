from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Department
from .serializers import UserSerializer, DepartmentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

# Create your views here.

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_approved:
            raise AuthenticationFailed("User not approved yet")
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role not in ['super_admin', 'super_admin_maker', 'admin_maker']:
            return Response({'error': 'Not allowed to create users'}, status=403)
        return super().create(request, *args, **kwargs)

@action(detail=True, methods=['post'])
def approve(self, request, pk=None):
    user = self.get_object()
    if request.user.role not in ['super_admin_checker', 'admin_checker']:
        return Response({'error': 'Only checkers can approve users'}, status=403)
    user.is_approved = True
    user.save()
    return Response({'message': 'User approved successfully'})

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         if request.role not in ['super_admin', 'super_admin_maker', 'super_admin_checker']:
#             return Response({'error': 'You do not have permission to create users.'}, status=403)
#         # Custom logic before creating the user
#         return super().create(request, *args, **kwargs)
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role != 'super_admin_maker':
            return Response({'error': 'Only Super Admin Maker can create departments'}, status=403)
        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Department created. Waiting for approval."}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        if request.user.role != 'super_admin_checker':
            return Response({'error': 'Only Super Admin Checker can approve departments'}, status=403)
        department = self.get_object()
        department.is_approved = True
        department.approved_by = request.user
        department.save()
        return Response({'message': 'Department approved successfully'})
    
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()  # Assuming you want to list all users for department view
#     serializer_class = UserSerializer  # Use the appropriate serializer for your department model
#     permission_classes = [permissions.IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         if request.role not in ['super_admin', 'super_admin_maker', 'super_admin_checker']:
#             return Response({'error': 'You do not have permission to create departments.'}, status=403)
#         # Custom logic before creating the department
#         return super().create(request, *args, **kwargs)