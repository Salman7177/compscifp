class Scrollbar(object):
    
    def __init__(self, posts, position, max_pos):
        self.x = 0
        self.y = 0
        self.num_posts = len(posts)
        self.bar_size = 0
        self.scroll_pos = position
        self.max_scroll = max_pos
    
    def display(self):    
        self.bar_size = height
        if self.num_posts * 200 - height > height:
            self.bar_size = height - 180 * log(self.num_posts)
            if self.bar_size < 20:
                self.bar_size = 20
        self.y = map(self.scroll_pos, 0, (self.num_posts * -200) + height, 0, height - self.bar_size)
        rect(1200, self.y, 80, self.bar_size)
        
