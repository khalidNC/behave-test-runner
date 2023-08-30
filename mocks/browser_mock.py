from mocks.api_mock import APIMock


class Browser:
    def __init__(self, url: str):
        self.url = url
        self.response = None
        self.user_list = []

    def visit_users_page(self):
        api = APIMock()
        api.request('GET', '/api/v1/users')
        response = api.get_response_json()
        self.user_list = response['data']

    def find_object(self, object_name: str):
        if object_name == 'user_list':
            return self.user_list
        if object_name == 'admin_count':
            admin_count = len([user for user in self.user_list if user['role'] == 'Administrator'])
            return admin_count
        return None

    def reset(self):
        self.response = None
        self.user_list = []
