import json

class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def convert_to_json(self, hashed_psswd):
        fp = "data/users-info.json"
        file_json = open(fp)
        crue = json.load(file_json)
        crue_2nd = crue["users"]
        
        crue_2nd.append({
                "password": hashed_psswd,
                "username": self.username,
                })
        

        user_dict = {"users":crue_2nd}        
        
        with open(fp, "w") as file_json:
            json.dump(user_dict, file_json, ensure_ascii=False, indent=4)
            file_json.write("\n")

    
        
