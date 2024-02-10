from django.db import models


class Folder(models.Model):
    name = models.CharField(("name"), max_length=100, blank=False, null=False, unique=False)
    parentFolderId = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class File(models.Model):
    name = models.CharField(("name"), max_length=100, blank=False, null=False, unique=False)
    content = models.TextField(("content"), null=False, blank=False)
    parentFolderId = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True,  default=None)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



