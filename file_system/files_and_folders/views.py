from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from files_and_folders.models import Folder, File
from files_and_folders.serializers import FolderSerializer, FileSerializer
from rest_framework.response import Response
from django.db.models import Q


@api_view(["POST"])
def create_folder(request):
    if request.method == "POST":
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def folder_actions(request, pk):
    try:
        folder = Folder.objects.get(pk=pk)
    except Folder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_file(request):
    if request.method == "POST":

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def file_actions(request, pk):

    try:
        file = File.objects.get(pk=pk)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FileSerializer(file)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def getFileSystemStructure(request):
    if request.method == "GET":
        child_folders = FolderSerializer(
            Folder.objects.filter(parentFolderId=None), many=True
        ).data
        child_files = FileSerializer(
            File.objects.filter(parentFolderId=None), many=True
        ).data

        response_data = {
            "name": "",
            "parentFolderId": None,
            "items": child_folders + child_files,
        }

        return Response(response_data)


@api_view(["GET"])
def getFolderObjects(request, pk):
    try:
        folder = Folder.objects.get(pk=pk)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        child_files = FileSerializer(folder.childFiles.all(), many=True).data
        child_folders = FolderSerializer(folder.childFolders.all(), many=True).data

        response_data = {
            "name": folder.name,
            "parentFolderId": (
                folder.parentFolderId.pk if folder.parentFolderId else None
            ),
            "items": child_folders + child_files,
        }

        return Response(response_data)


@api_view(["GET"])
def searchForObjects(request, query=""):
    if request.method == "GET":
        files = File.objects.all()
        folders = Folder.objects.all()

        if query:
            files = FileSerializer(
                files.filter(Q(name__icontains=query) | Q(content__icontains=query))[
                    :5
                ],
                many=True,
            ).data
            folders = FolderSerializer(
                folders.filter(name__icontains=query)[:5], many=True
            ).data

            return Response(files + folders)
        return Response([])
