# Generated by Django 5.0.2 on 2024-02-10 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_and_folders', '0003_alter_file_parentfolderid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='parentFolderId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childFiles', to='files_and_folders.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parentFolderId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childFolders', to='files_and_folders.folder'),
        ),
    ]
