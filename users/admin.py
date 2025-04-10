from django.contrib import admin
from .models import User, Department

# Register your models here.

admin.site.register([
    User,
    Department,
])
# admin.site.site_header = "File Management System Admin"
# admin.site.site_title = "File Management System Admin Portal"
# admin.site.index_title = "Welcome to the File Management System Admin Portal"