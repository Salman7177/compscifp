from scrollbar import Scrollbar
posts = []
bar = []
scroll_pos = 0


def setup():
    global posts, max_scroll
    size(1280, 720)
    for i in range(10):
        posts.append("lol")
    max_scroll = (len(posts) * -200) + height
    bar.append(Scrollbar(posts, scroll_pos, max_scroll))
        
def draw():
    background(100)
    for i in range(len(posts)):
        rect(width/2, (200 * i) + scroll_pos, 300, 200)
    for i in bar:
        i.scroll_pos = scroll_pos
        i.display()
        
        
def mouseWheel(event):
    global scroll_pos, posts
    
    scroll_pos -= event.getCount() * 25
    if scroll_pos > 0:
        scroll_pos = 0
    elif scroll_pos < max_scroll:
        scroll_pos = max_scroll
    
