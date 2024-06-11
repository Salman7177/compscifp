import json

class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def hash_password(self):
        for i in self.password:
            if i.isdigit():
                hashmap = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
                hex_str = ''
                    
                if int(i) == 0:
                    return "0"
                
                while int(self.password) > 0:
                    hex_val = int(i) % 16
                    num = int(i) // 16
                    
                    if hex_val >= 10:
                        hex_str = hashmap[hex_val] + hex_str
                    else:
                        hex_str = str(hex_val) + hex_str    
                print(hex_str)
            else:
                print(ord(i))            
    
    def convert_to_json(self):
        
        file_json = open("UserInformation.json", "a")
            
        User = {
                "username": self.username,
                "password": self.password
                }
        
        jsonified_user = json.dumps(User, indent=4)
        # print(jsonified_user)
        
        parsed_json = json.loads(jsonified_user)
                
        file_json.write(str(jsonified_user))
        file_json.close()
        
        # print(parsed_json["username"])    
                
    


        
