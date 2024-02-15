from django.contrib import admin
from django.urls import path
from files_and_folders import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.getFileSystemStructure, name="rottObjects"),
    path("folders/", views.create_folder, name="createFolder"),
    path("folders/<int:pk>", views.folder_actions, name="folderActions"),
    path("files/", views.create_file, name="createFile"),
    path("files/<int:pk>", views.file_actions, name="filesActions"),
    path("folders/<int:pk>/objects", views.getFolderObjects, name="folderObjects"),
    path("search/", views.searchForObjects, name="searchNoQuery"),
    path("search/<str:query>", views.searchForObjects, name="search"),
]
