class Browser:
    def __init__(self, url: str):
        self.url = url
        self.api = API(self.url)
        self.response = None
 
 
    def request(self, http_method: str, endpoint: str):
          self.response = self.api.request(http_method, endpoint)
 
    def find_object(self, object_name: str):
        if object_name in self.response:
            return self.response[object_name]
        return None
 
mock_actions = "Mock value for actions"
 
class API:
    def __init__(self, url: str):
        self.url = url
 
    def request(self, http_method: str, endpoint: str):
        if http_method == 'GET' and endpoint == "/api/v1/users":
            # Simulate making API request and handling response
            response = {
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
            return response
        else:
            return None
 
# Creating instances of the classes
website_url = "https://myweb.com"
api_url = "https://api.myweb.com"
 
browser = Browser(api_url)
browser.request("GET", "/api/v1/users")
# Using the instances to perform actions
user_list = browser.find_object("data")

print(user_list)
