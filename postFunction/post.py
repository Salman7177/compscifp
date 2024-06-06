import json

class postFunction(object):
    def __init__(self, id, username, post_txt):
        self.id = id
        self.username = username
        self.post_txt = post_txt
        
    def convert_post_to_json(self, all_posts):
        output = createWriter("data/posts.json")
        
        posts_list = [{"id": post.id, "username": post.username, "post_txt": post.post_txt} for post in all_posts]
        
        jsonified_posts = json.dumps(posts_list, indent=4)
        print(jsonified_posts)
        
        output.write(jsonified_posts)
        output.flush()
        output.close()
