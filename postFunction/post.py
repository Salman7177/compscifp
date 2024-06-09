import json

class postFunction(object):
    def __init__(self, id, username, title, post_txt):
        self.id = id
        self.username = username
        self.title = title
        self.post_txt = post_txt
    
    def convert_post_to_json(self, post):
        print("h")
        file_json = open("data/posts.json", "a")

        post_dict = {"id": post.id, "username": post.username, "title": post.title, "post_txt": post.post_txt}
        print(post)
        
        with open("data/posts.json", "a") as file_json:
            json.dump(post_dict, file_json, indent=4)
            file_json.write("\n")
        
