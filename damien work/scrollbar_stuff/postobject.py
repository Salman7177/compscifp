class post_object(object):
    
    def __init__(self, id, title, contents):
        self.y = 0
        self.id = id
        self.title = title
        self.contents = contents
    
    def draw_posts(self):
        rect(width/2, self.y, width/3, 200)
        
        
