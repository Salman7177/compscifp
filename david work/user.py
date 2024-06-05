import json

class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def convert_to_json(self):
        output = createWriter("data/UserInformation.json")
        User = {
                "username": self.username,
                "password": self.password
                }
        jsonified_user = json.dumps(User)
        print(jsonified_user)
        output.append(jsonified_user)
        output.flush()
        output.close()
    
    def hash_password(self):
        pass
        
