import json

class postFunction(object):
    def __init__(self, id, username, title, post_txt):
        self.id = id
        self.username = username
        self.title = title
        self.post_txt = post_txt
    
    def convert_post_to_json(self, post):
        print("H")
        fp = "data/posts.json"
        file_json = open(fp)
        crue = json.load(file_json)
        crue_2nd = crue["posts"]
        crue_2nd.append({"id": post.id, "user": post.username, "title": post.title, "post_txt": post.post_txt})
        print(crue_2nd)
        
        post_dict = {"posts":crue_2nd}
    
        with open(fp, "w") as file_json:
            json.dump(post_dict, file_json, ensure_ascii=False, indent=4)
            file_json.write("\n")
