from rest_framework import serializers
from .models import User, Department
import random
import string
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'department', 'is_approved']

    def create(self, validated_data):
        raw_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        user = User(**validated_data)
        user.set_password(raw_password)
        user.temporary_password = raw_password
        user.save()
        # Optional: Send email here with temp password

        send_mail(
            subject='Temporary Password',
            message=f'Your temporary password is: {raw_password}',
            from_email= None,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return user

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'department', 'is_approved']
#         read_only_fields = ['id']  # Make the id field read-only

#     def create(self, validated_data):
#         # Generate a temporary password
#         temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#         validated_data['temporary_password'] = temp_password
#         user = super().create(validated_data)
#         user.set_password(temp_password)
#         user.save()
#         # Send email with the temporary password here if needed
#         # send_email_with_temp_password(user.email, temp_password)

#         return user
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'created_at', 'updated_at', 'is_approved', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at']  # Make the id, created_at, and updated_at fields read-only

    def create(self, validated_data):
        department = super().create(validated_data)
        return department