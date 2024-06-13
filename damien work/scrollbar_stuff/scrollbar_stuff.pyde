import json
from scrollbar import Scrollbar
from postobject import post_object
# the scrollbar works off a set list and scroll position based on the main program. you'll have to set that up once we bring everything together.

# the scrollbar needs a set list of posts and a scroll position to work off of.
posts = []
bar = []
scroll_pos = 0

# put in setup as an example, but when we switch pages i must have a list of posts defined so creating the scrollbar can read from it and determine its length.
def setup():
    global posts, max_scroll
    size(1280, 720)
    
    file_json = open("posts.json")
    loaded_posts = json.load(file_json)
    
    for i in loaded_posts["posts"]:
        cur_post = post_object(i["id"], i["title"], i["post_txt"])
        posts.append(cur_post)
    
    max_scroll = (len(posts) * -200) + height # Max scroll should add up all the heights of each individual post box and subtract the height to make sure it ends at the last post.
    bar.append(Scrollbar(posts, scroll_pos, max_scroll))

#example boxes, for i in bar sets the internal scroll position to the global scroll position and updates its position.
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
        
# mousewheel scrolling script, if we ever do multiple scrollbars make sure that the user is selected or hovering over the element they want to scroll over.    
def mouseWheel(event):
    global scroll_pos, posts
    
    scroll_pos -= event.getCount() * 25
    if scroll_pos > 0:
        scroll_pos = 0
    elif scroll_pos < max_scroll:
        scroll_pos = max_scroll
    
