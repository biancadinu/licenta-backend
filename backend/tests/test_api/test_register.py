from tests.base_test import BaseTest


class TestRegister(BaseTest):

    def test_register(self):
        response = self.client.post('/register/',
                                    {'username': 'test', 'password': 'P@ssw0rd', 'email': 'email@email.com',
                                     'first_name': 'Test', 'last_name': 'User'})
        self.assertEqual(201, response.status_code)
