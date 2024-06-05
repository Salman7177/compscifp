import json

class postFunction(object):
    def __init__(self, id, username, post_txt):
        self.id = id
        self.username = username
        self.post_txt = post_txt
        
    def convert_post_to_json(self):
        
        output = createWriter("data/posts.json")
        
        Post = {
                "id": self.id,
                "username": self.username,
                "post_txt": self.post_txt
                }
        
        jsonified_post = json.dumps(Post)
        print(jsonified_post)
        
        output.append(jsonified_post + "\t")
        output.flush()
        output.close()
