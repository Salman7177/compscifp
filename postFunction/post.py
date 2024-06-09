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
            # Convert the post_dict to JSON and write it to the file
            json.dump(post_dict, file_json, indent=4)
            file_json.write("\n")
        
        # jsonified_posts = json.dumps(posts_list, indent=4)
        
        # print(jsonified_posts)
        
        # file_json.write(str(jsonified_posts))
        # file_json.flush()
        # file_json.close()
        
        
