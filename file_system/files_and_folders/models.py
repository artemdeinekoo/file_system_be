from django.db import models
from sys import getsizeof


class Folder(models.Model):
    name = models.CharField(
        ("name"), max_length=100, blank=False, null=False, unique=False
    )
    parentFolderId = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="childFolders",
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    @property
    def byte_size(self):
        byte_size = 0

        for file in self.childFiles.all():
            byte_size += file.byte_size

        for folder in self.childFolders.all():
            byte_size += folder.byte_size

        return byte_size


class File(models.Model):
    name = models.CharField(
        ("name"), max_length=100, blank=False, null=False, unique=False
    )
    content = models.TextField(("content"), null=False, blank=False)
    parentFolderId = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="childFiles",
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    @property
    def byte_size(self):
        return getsizeof(self.content)
