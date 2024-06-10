import json

class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def convert_to_json(self):
        
        file_json = open("UserInformation.json", "a")
            
        User = {
                "username": self.username,
                "password": self.password
                }
        
        jsonified_user = json.dumps(User, indent=4)
        print(jsonified_user)
        
        parsed_json = json.loads(jsonified_user)
                
        file_json.write(str(jsonified_user))
        file_json.close()
<<<<<<< HEAD
    
        print(parsed_json["username"])
                

            

=======
        
    def hash_password(self):
        pass
>>>>>>> a1da13af0f97a015a4303322230d1052c369b18a
        
