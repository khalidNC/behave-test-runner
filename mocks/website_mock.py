from features.browser import mock_actions


class WebsiteMock:
    def __init__(self):
        self.user_list = []
        self.admin_count = 0

    def visit_users_page(self):
        self.user_list = [
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
        ]
        self.admin_count = 1

    def find_object(self, object_name):
        if object_name == 'user_list':
            return self.user_list
        elif object_name == 'admin_count':
            return self.admin_count

    def reset(self):
        self.user_list = []
        self.admin_count = 0
