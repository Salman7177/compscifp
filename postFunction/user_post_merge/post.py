import json

class postFunction(object):
    def __init__(self, id, username, title, post_txt):
        self.id = id
        self.username = username
        self.title = title
        self.post_txt = post_txt
    
    def convert_post_to_json(self, post):
        
        print("h")
        file_json = open("data/posts.json")
        crue = json.load(file_json)
        crue_2nd = crue["posts"]
        print(crue_2nd)
        crue_2nd.append({"id": post.id, "title": post.title, "post_txt": post.post_txt})
        print(crue_2nd)
        
        
        post_dict = {"posts":crue_2nd}
        print(post)
        
        
        with open("data/posts.json", "w") as file_json:
            json.dump(post_dict, file_json, ensure_ascii=False, indent=4)
            file_json.write("\n")
    
    # def convert_post_to_json(self, all_posts):
    #     output = createWriter("data/posts.json")
    #     # print(jsonified_posts)

    #     posts_list = [{"id": post.id, "username": post.username, "title": post.title, "post_txt": post.post_txt}]
    #     # file_json.write(str(jsonified_posts))
    #     # file_json.flush()
    #     # file_json.close()

    #     jsonified_posts = json.dumps(posts_list, indent=4)
    #     print(jsonified_posts)

    #     output.write(jsonified_posts)
    #     output.flush()
    #     output.close()


# The way this is done isn't readable sob emoji sob emoji
# This needs to be done by putting all the contents in an array, so we have to break everything apart and readd it to an array rather than appending it to the file.
