from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_add_folder_to_root_no_data(self):
        res = self.client.post(self.add_folder_url)
        self.assertEqual(res.status_code, 400)

    def test_add_folder_to_root(self):
        res = self.client.post(
            self.add_folder_url, self.folder_data_no_parentFolder, format="json"
        )
        self.assertEqual(res.status_code, 201)

    def test_add_folder_to_folder(self):
        self.client.post(
            self.add_folder_url, self.folder_data_no_parentFolder, format="json"
        )
        res = self.client.post(
            self.add_folder_url, self.folder_data_parentFolder, format="json"
        )

        self.assertEqual(res.status_code, 201)

    def test_add_folder_to_unexisting_folder(self):
        res = self.client.post(
            self.add_folder_url,
            self.folder_data_parentFolderId_notexists,
            format="json",
        )

        self.assertEqual(res.status_code, 400)
