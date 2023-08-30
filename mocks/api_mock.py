
class APIMock:
    def __init__(self):
        self.status_code = 0
        self.response_json = {}

    def request(self, http_method, endpoint):
        if http_method == 'GET' and endpoint == '/api/v1/users':
            mock_actions = object()
            self.status_code = 200
            self.response_json = {
                "data": [
                    {"last_name": "Admin", "first_name": "Mr", "email": "admin@uniq.app", "confirmed": True,
                     "role": "Administrator", "other_permissions": "N/A", "social": "None", "last_updated": 8,
                     "actions": mock_actions},
                    {"last_name": "User", "first_name": "Teacher", "email": "teacher@uniq.app", "confirmed": True,
                     "role": "Teacher", "other_permissions": "N/A", "social": "None", "last_updated": 4,
                     "actions": mock_actions},
                    {"last_name": "User", "first_name": "Student", "email": "student@uniq.app", "confirmed": True,
                     "role": "Student", "other_permissions": "N/A", "social": "None", "last_updated": 4,
                     "actions": mock_actions},
                    {"last_name": "User", "first_name": "Normal", "email": "user@uniq.app", "confirmed": True,
                     "role": "Student", "other_permissions": "N/A", "social": "None", "last_updated": 4,
                     "actions": mock_actions}
                ],
                "Meta": {"total": 4, "limit": 10, "offset": 0}
            }

    def get_status_code(self):
        return self.status_code

    def get_response_json(self):
        return self.response_json

    def reset(self):
        self.status_code = 0
        self.response_json = {}
