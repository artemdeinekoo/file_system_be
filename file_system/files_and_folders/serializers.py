from rest_framework import serializers
from files_and_folders.models import Folder, File
from rest_framework.validators import UniqueValidator


class FolderSerializer(serializers.ModelSerializer):
    byteSize = serializers.SerializerMethodField("getByteSize")
    isFolder = serializers.BooleanField(default=True, read_only=True)

    def getByteSize(self, model):
        return model.byte_size

    class Meta:
        model = Folder
        fields = [
            "id",
            "name",
            "parentFolderId",
            "createdAt",
            "updatedAt",
            "byteSize",
            "isFolder",
        ]

    def validate(self, data):

        if Folder.objects.filter(parentFolderId=None, name=data["name"]):
            raise ValueError("Folder with this name already exists in the directory")

        elif "parentFolderId" in data and Folder.objects.filter(
            parentFolderId=data["parentFolderId"], name=data["name"]
        ):
            raise ValueError("Folder with this name already exists in the directory")
        return data


class FileSerializer(serializers.ModelSerializer):
    byteSize = serializers.SerializerMethodField("getByteSize")
    isFolder = serializers.BooleanField(default=False, read_only=True)

    def getByteSize(self, model):
        return model.byte_size

    class Meta:
        model = File
        fields = [
            "id",
            "name",
            "content",
            "parentFolderId",
            "createdAt",
            "updatedAt",
            "byteSize",
            "isFolder",
        ]

    def validate(self, data):

        if File.objects.filter(parentFolderId=None, name=data["name"]):
            raise ValueError("File with this name already exists in the directory")

        elif "parentFolderId" in data and File.objects.filter(
            parentFolderId=data["parentFolderId"], name=data["name"]
        ):
            raise ValueError("File with this name already exists in the directory")

        return data
