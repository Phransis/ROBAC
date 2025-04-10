from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'
    #     model = models.File
    #     fields = ['id', 'file', 'uploaded_at', 'user']
    #     read_only_fields = ['id', 'uploaded_at', 'user']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     return super().create(validated_data)

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Folder
        fields = '__all__'
    #     model = models.Folder
    #     fields = ['id', 'name', 'created_at', 'updated_at', 'user']
    #     read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     return super().create(validated_data)