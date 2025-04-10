from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('super_admin_maker', 'Super Admin Maker'), # Department Admin Maker
        ('super_admin_checker', 'Super Admin Checker'), # Department Admin Checker
        ('admin_maker', 'Admin Maker'), # Department Admin 
        ('admin_checker', 'Admin Checker'),
        ('user', 'User'),   
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    temporary_password = models.CharField(max_length=255, blank=True, null=True)
    # is_super_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'role']

    def __str__(self):
        return f"{self.username} - {self.get_full_name()} - {self.role}"

class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='approved_departments')
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name