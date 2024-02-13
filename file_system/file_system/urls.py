from django.contrib import admin
from django.urls import path
from files_and_folders import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.getFileSystemStructure),
    path("folders/", views.create_folder),
    path("folders/<int:pk>", views.folder_actions),
    path("files/", views.create_file),
    path("files/<int:pk>", views.file_actions),
    path("folders/<int:pk>/objects", views.getFolderObjects),
]
