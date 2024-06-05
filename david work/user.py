import json
class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def convert_to_json(self):
        output = createWriter("UserInformation.json")
        
        with open("UserInformation.json", "a") as userinfohere:
                User = {
                        "username": self.username,
                        "password": self.password
                        }
                jsonified_user = json.dumps(User)
                print(jsonified_user)
                userinfohere.write(jsonified_user)
                
        # else:
        #     User = {
        #         "username": self.username,
        #         "password": self.password
        #         }
            
        #     jsonified_user = json.dumps(User)
        #     userinfo.wirte(jsonified_user)
                
        #     output.append(jsonified_user)
        #     output.flush()
        #     output.close()
            
        
    def hash_password(self):
        pass
        
