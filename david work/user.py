import json
from pathlib import Path

class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def convert_to_json(self):
        output = createWriter("data/UserInformation.json")
        output_path = Path("data/UserInformation.json")
        
        if output_path.is_file():
            with open("data/UserInformation.json", "a") as userinfo:
                
                User = {
                        "username": self.username,
                        "password": self.password
                        }
                jsonified_user = json.dumps(User)
                print(jsonified_user)
                userinfo.wirte(jsonified_user)
                
        else:
            User = {
                "username": self.username,
                "password": self.password
                }
            
            jsonified_user = json.dumps(User)
            userinfo.wirte(jsonified_user)
                
            output.append(jsonified_user)
            output.flush()
            output.close()
            
        
    def hash_password(self):
        pass
        
