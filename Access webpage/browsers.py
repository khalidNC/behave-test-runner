class Browser:
    def __init__(self, url: str):
        self.url = url
    
    def find_object(self, object_name: str):
        if object_name == "user_list":
            # Simulate interacting with the user list
            print(f"Interacting with user list on {self.url}")
        else:
            print(f"Object '{object_name}' not found on {self.url}")

class API:
    def __init__(self, url: str):
        self.url = url
    
    def request(self, http_method: str, endpoint: str):
        if endpoint == "/api/v1/users":
            # Simulate making API request and handling response
            response = {
                "data": [
                    {"last_name": "Admin", "first_name": "Mr", "email": "admin@uniq.app", "confirmed": True, 
                     "role": "Administrator", "other_permissions": "N/A", "social": "None", "last_updated": 8},
                    {"last_name": "User", "first_name": "Teacher", "email": "teacher@uniq.app", "confirmed": True, 
                     "role": "Teacher", "other_permissions": "N/A", "social": "None", "last_updated": 4},
                    {"last_name": "User", "first_name": "Student", "email": "student@uniq.app", "confirmed": True, 
                     "role": "Student", "other_permissions": "N/A", "social": "None", "last_updated": 4},
                    {"last_name": "User", "first_name": "Normal", "email": "user@uniq.app", "confirmed": True, 
                     "role": "Student", "other_permissions": "N/A", "social": "None", "last_updated": 4}
                ],
                "Meta": {"total": 4, "limit": 10, "offset": 0}
            }
            print(f"Making a {http_method} request to API endpoint '{endpoint}' at {self.url}")
            print("API Response:", response)
        else:
            print(f"API endpoint '{endpoint}' not found at {self.url}")

# Creating instances of the classes
website_url = "https://myweb.com"
api_url = "https://api.myweb.com"

browser = Browser(website_url)
api = API(api_url)

# Using the instances to perform actions
browser.find_object("user_list")
api.request("GET", "/api/v1/users")

