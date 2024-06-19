import json

class bioFunction(object):
    def __init__(self, username, txt):
        self.txt = txt
        self.username = username
    
    def write_bio_to_json(self, new_bio):
    
        fp = "data/bio.json"
        file_json = open(fp)
        crue = json.load(file_json)
        crue_2nd = crue["user"]
        crue_2nd.append({"user": new_bio.username, "bio": new_bio.txt})
        bio_dict = {"user":crue_2nd}        
        
        with open(fp, "w") as file_json:
            json.dump(bio_dict, file_json, ensure_ascii=False, indent=4)
            file_json.write("\n")
    
        print("h")
