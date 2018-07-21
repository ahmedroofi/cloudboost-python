from CBUrls import CBUrls
from CBRequests import CBRequests


class CBUser(object):

    default_password = "Password1"

    def __init__(self, key, app_id, url):
        self.key = key
        self.url = CBUrls(url, app_id)
        self.api = CBRequests()

    def user_signup_data(self, username, email, password):
        if not password:
            password = self.default_password
        return {"_type": "user",
                "username": username,
                "expires": None,
                "email": email,
                "_modifiedColumns": ["createdAt",
                                     "updatedAt",
                                     "ACL",
                                     "expires",
                                     "username",
                                     "password",
                                     "email"],
                "_tableName": "User",
                "ACL": {
                    "write": {
                        "allow": {
                            "role": [],
                            "user": ["all"]
                        },
                        "deny": {
                            "role": [],
                            "user": []
                        }
                    },
                    "read": {
                        "allow": {
                            "role": [],
                            "user": ["all"]
                        },
                        "deny": {
                            "role": [],
                            "user": []
                        }
                    }
                },
                "password": password,
                "_isModified": True
                }

    def signup_user(self, username, email, password=None):
        data = {
            "key": self.key,
            "document": self.user_signup_data(username, email, password)
        }
        response = self.api.post_request(self.url.get_signup_url(), data)
        return response
