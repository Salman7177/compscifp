import json

class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    # def hash_password(self, passwd):
    #     new_psswd = ""
    #     for i in passwd:
    #         new_psswd += str(ord(i))
    #     return new_psswd    
    
    def convert_to_json(self, hashed_psswd):
        

        file_json = open("UserInformation.json", "a")
            
        User = {
                "username": self.username,
                "password": hashed_psswd,
                }
        
        jsonified_user = json.dumps(User, indent=4)

        
        parsed_json = json.loads(jsonified_user)
                
        file_json.write(str(jsonified_user))
        file_json.close()
        
        
        
        print(jsonified_user)    
                
    


        
