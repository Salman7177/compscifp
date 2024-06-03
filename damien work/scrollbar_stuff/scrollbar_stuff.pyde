# scrollbar to be imported
#
#the scrollbar should be able to see the height of a post for scroll calculations
#x and y of a post must be accessed
#
#

posts = []
scroll_pos = 0


def setup():
    global posts
    size(1280, 720)
    for i in range(10):
        posts.append("lol")
        
def draw():
    background(100)
    for i in range(len(posts)):
        rect(width/2, (200 * i) + scroll_pos, 300, 200)
        
        
def mouseWheel(event):
    global scroll_pos, posts
    max_scroll = (len(posts) * -200) + 720
    
    scroll_pos -= event.getCount() * 25
    if scroll_pos > 0:
        scroll_pos = 0
    elif scroll_pos < max_scroll:
        scroll_pos = max_scroll
    

def drawScrollbar():
    global posts, scroll_pos
    
    max_dist = (len(posts) * 200) + -720
