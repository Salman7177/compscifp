# scrollbar to be imported
#
#the scrollbar should be able to see the height of a post for scroll calculations
#x and y of a post must be accessed
#
#

#TODO: Click and drag.

posts = []
scroll_pos = 0


def setup():
    global posts
    size(1280, 720)
    for i in range(30):
        posts.append("lol")
        
def draw():
    background(100)
    for i in range(len(posts)):
        rect(width/2, (200 * i) + scroll_pos, 300, 200)
    drawScrollbar()
        
        
def mouseWheel(event):
    global scroll_pos, posts
    max_scroll = (len(posts) * -200) + height
    
    scroll_pos -= event.getCount() * 25
    if scroll_pos > 0:
        scroll_pos = 0
    elif scroll_pos < max_scroll:
        scroll_pos = max_scroll
    

def drawScrollbar():
    global posts, scroll_pos
    bar_size = height
    # when do y pos, check from the lowest point all the way to the end.
    if len(posts) * 200 - height > height:
        bar_size = height - 180 * log(len(posts))
        if bar_size < 20:
            bar_size = 20
    
    rect(1200, map(scroll_pos, 0, (len(posts) * -200) + height, 0, height - bar_size), 80, bar_size)
        
