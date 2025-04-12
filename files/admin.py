from django.contrib import admin
from .models import File, FileAccessLog, Folder

# Register your models here.
admin.site.register([
    File,
    FileAccessLog,
    Folder,
])
admin.site.site_header = "ROPAC Admin"
admin.site.site_title = "ROPAC Admin Portal"
admin.site.index_title = "Welcome to the ROPAC Admin Portal"
