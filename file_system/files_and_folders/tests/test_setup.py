from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.add_folder_url = reverse("createFolder")
        self.add_file_url = reverse("createFile")

        self.folder_data_no_parentFolder = {"name": "test"}
        self.folder_data_parentFolder = {"name": "test", "parentFolderId": 1}
        self.folder_data_parentFolderId_notexists = {
            "name": "test",
            "parentFolderId": 1,
        }
        self.folder_edit_name = {"name": "edited"}

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
