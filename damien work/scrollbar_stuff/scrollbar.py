class Scrollbar(object):
    
    # Initial variables
    def __init__(self, posts, position, max_pos):
        self.y = 0
        self.num_posts = posts # Determines how long the bar should be.
        self.bar_size = 0 # The actual bar size
        self.scroll_pos = position # The scroll position from the global value.
        self.max_scroll = max_pos # Highest scroll position value from the global script.
    
    # Determines the size it should set itself and displays the bar based on scroll position and number of posts.
    def display(self): 
        fill(255)   
        if self.num_posts > 3:
            self.bar_size = height - 180 * log(self.num_posts)
            if self.bar_size < 20:
                self.bar_size = 20
        self.y = map(self.scroll_pos, 0, (self.num_posts * -200) + height, 0, height - self.bar_size)
        rect(1250, self.y, 30, self.bar_size, 20)
        
