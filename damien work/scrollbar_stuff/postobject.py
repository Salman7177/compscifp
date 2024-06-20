class post_object(object):
    
    # Setup variables
    def __init__(self, id, title, contents):
        self.y = 0
        self.id = id
        self.title = title
        self.contents = contents
    
    # Draws the post box based off of given data and scroll position. Delimiter replaces the "|" with a "\n" to make a new line.
    def draw_posts(self):
        fill(255)
        rect(250, self.y, 1030, 200)
        fill(0)
        textSize(24)
        text(self.title + " - " + self.id, 270, self.y + 30)
        textSize(16)
        new_string = self.contents.replace("|", "\n")
        text(new_string, 270, self.y + 60, 950, 150)
        
        
