from django.contrib import admin
from .models import File, FileAccessLog, Folder

# Register your models here.
admin.site.register([
    File,
    FileAccessLog,
    Folder,
])
admin.site.site_header = "File Management System Admin"
admin.site.site_title = "File Management System Admin Portal"
admin.site.index_title = "Welcome to the File Management System Admin Portal"
