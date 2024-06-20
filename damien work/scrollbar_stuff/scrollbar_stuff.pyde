# Imported libraries
import json
from scrollbar import scrollbar
from postobject import post_object


# Global variables to keep track of classes made and page position
posts = []
bar = []
scroll_pos = 0

# Loads all the posts and creates a class using the data from the json. In the JSON file, "id" is unused.
def setup():
    global posts, max_scroll
    size(1280, 720)
    
    file_json = open("posts.json")
    loaded_posts = json.load(file_json)
    
    for i in loaded_posts["posts"]:
        cur_post = post_object(i["username"], i["title"], i["post_txt"])
        posts.insert(0, cur_post)
    
    max_scroll = (len(posts) * -200) + height # Max scroll should add up all the heights of each individual post box and subtract the height to make sure it ends at the last post.
    bar.append(scrollbar(len(posts), scroll_pos, max_scroll))

# Draws the posts and scrollbar based off of scroll position
def draw():
    global posts
    num_posts = 0
    background(100)
    for i in posts:
        i.y = (200 * num_posts) + scroll_pos
        i.draw_posts()
        num_posts += 1
    for i in bar:
        i.scroll_pos = scroll_pos
        i.display()
        
# Adds or subtracts the scroll position on mousewheel. 
def mouseWheel(event):
    global scroll_pos, posts, max_scroll
    
    if max_scroll < 0:
        scroll_pos -= event.getCount() * 25
        if scroll_pos > 0:
            scroll_pos = 0
        elif scroll_pos < max_scroll:
            scroll_pos = max_scroll
    
