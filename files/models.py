from django.db import models

# Create your models here.

class File(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('restricted', 'Restricted'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    visibility = models.CharField(max_length=50, choices=VISIBILITY_CHOICES, default='private')
    allowed_users = models.ManyToManyField('users.User', related_name='allowed_files', blank=True)
    is_deleted = models.BooleanField(default=False)

def __str__(self):
        return f"{self.name} - {self.uploaded_by.username} - {self.uploaded_at}"
    # def get_file_size(self):
    #     return self.file.size
    # def get_file_extension(self):
    #     return self.file.name.split('.')[-1]


class FileAccessLog(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    accessed_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    accessed_at = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)  # e.g., 'downloaded', 'viewed', etc.

class Folder(models.Model):
    name = models.CharField(max_length=255)
    visibility = models.CharField(max_length=50, choices=File.VISIBILITY_CHOICES, default='private')
    description = models.TextField(blank=True, null=True)
    departmet = models.ForeignKey('users.Department', on_delete=models.CASCADE, blank=True, null=True)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subfolders')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    allowed_users = models.ManyToManyField('users.User', related_name='allowed_folders', blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.created_by.username} - {self.created_at}"