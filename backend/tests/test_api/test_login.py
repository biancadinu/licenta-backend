from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_log_in_successful(self):
        response = self.client.post('/auth/',
                                    data={'username': self.superuser.username, 'password': self.common_password})
        self.assertEqual(200, response.status_code)
        self.assertEqual(221, len(response.data['token']))

    def test_log_in_unsuccessful(self):
        response = self.client.post('/auth/', username='wrong_username', password=self.common_password)
        self.assertEqual(400, response.status_code)
