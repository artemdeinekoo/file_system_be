from rest_framework import serializers
from files_and_folders.models import Folder, File
from sys import getsizeof
from rest_framework.validators import UniqueValidator



class FolderSerializer(serializers.ModelSerializer):
    childFolders = serializers.SerializerMethodField('getChildFolders')
    childFiles = serializers.SerializerMethodField('getChildFiles')
 
    class Meta:
        model = Folder
        fields = ['id', 'name', 'parentFolderId', 'childFolders', 'childFiles', 'createdAt', 'updatedAt']

    def getChildFolders(self, obj):
        childFolders = Folder.objects.filter(parentFolderId=obj.id)
        return [folder.id for folder in childFolders]

    def getChildFiles(self, obj):
        child_files = File.objects.filter(parentFolderId=obj.id)
        return [file.id for file in child_files]

    def validate(self, data):
        
        if Folder.objects.filter(parentFolderId=None, name=data["name"]):
            raise ValueError("Folder with this name already exists in the directory")

        elif 'parentFolderId' in data and Folder.objects.filter(parentFolderId=data["parentFolderId"], name=data["name"]):
            raise ValueError("Folder with this name already exists in the directory")
        return data

    


class FileSerializer(serializers.ModelSerializer):
    byteSize = serializers.SerializerMethodField('getByteSize')

    class Meta:
        model = File
        fields = ['id', 'name', 'content', 'parentFolderId', 'createdAt', 'updatedAt', 'byteSize']

    def validate(self, data):
    
        if File.objects.filter(parentFolderId=None, name=data["name"]):
            raise ValueError("File with this name already exists in the directory")

        elif 'parentFolderId' in data and File.objects.filter(parentFolderId=data["parentFolderId"], name=data["name"]):
            raise ValueError("File with this name already exists in the directory")

        return data

    def getByteSize(self, obj):
        return getsizeof(obj)
    
class FileSystemSerializer(serializers.ModelSerializer):
    childFolders = serializers.SerializerMethodField('getChildFolders')
    childFiles = serializers.SerializerMethodField('getChildFiles')
    byteSize = serializers.SerializerMethodField('getByteSize')


    class Meta:
        model = Folder
        fields = ['id', 'name', 'parentFolderId', 'childFolders', 'childFiles', 'createdAt', 'updatedAt', 'byteSize']
    
    def getChildFolders(self, obj):
        childFolders = Folder.objects.filter(parentFolderId=obj.id)
        serializer = FileSystemSerializer(childFolders, many=True)
        return serializer.data

    def getChildFiles(self, obj):
        childFiles = File.objects.filter(parentFolderId=obj.id)
        serializer = FileSerializer(childFiles, many=True)
        return serializer.data

    def getByteSize(self, obj):
        return getsizeof(obj)