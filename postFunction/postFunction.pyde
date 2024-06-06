import json
from post import postFunction

users = ["Salman", "Damien", "David", "Shaheer"]
post_txt = ""
posts = []

temp_txt = ""
hold_txt = []
ty = 20
txtw = 0

enter_btn = [1185, 110, 90, 35, False]

grey = [54, 54, 54]


def setup():
    size(1280, 720)
    global txtw, temp_txt, tx, ty
    txtw = 0
    temp_txt = ""
    tx, ty = 310, 20
    noStroke()

def draw():
    background(240) 
    UserInterface()
    
    fill(0)
    textAlign(CENTER, CENTER)
    text(str(mouseX) + ", " + str(mouseY), width/2, height-10)
    textAlign(CORNER, CENTER)
    
    mouse_over_button_logic()
    
def mouse_over_button_logic():
    global enter_btn
    
    enter_btn[4] = mouseX > enter_btn[0] and mouseX < enter_btn[0] + enter_btn[2] and mouseY > enter_btn[1] and mouseY < enter_btn[1] + enter_btn[3]


    
    
    
    
    
    
    

def UserInterface():
    global temp_txt
    global tx, ty

    # Text Box
    fill(255)
    rect(300, 0, width - 300, 150)

    # Display typed text
    fill(0)
    textSize(15)
    
    # Display the held lines
    for i, line in enumerate(hold_txt):
        text(line, 310, 20 + i * 20)
    
    # Display the current typing line
    text(temp_txt, 310, ty)
    
    # Enter button
    fill(grey[0], grey[1], grey[2])
    rect(enter_btn[0], enter_btn[1], enter_btn[2], enter_btn[3])
    
    fill(255)
    textAlign(CORNER, CENTER)
    text("Post", 1217, 127)
    textAlign(CORNER, CENTER)
    
    
    
    

def keyPressed():
    global post_txt, temp_txt, hold_txt, ty, txtw

    if keyCode == SHIFT:
        pass
    elif key == BACKSPACE:
        if len(temp_txt) > 0:
            temp_txt = temp_txt[:-1]
        elif len(hold_txt) > 0:
            temp_txt = hold_txt.pop() + temp_txt
            ty -= 20
    elif key == ENTER:
        if len(hold_txt) < 5:  
            hold_txt.append(temp_txt)
            temp_txt = ""
            ty += 20
    else:
        temp_txt += key

    txtw = textWidth(temp_txt)
    if txtw > 960:
        hold_txt.append(temp_txt)
        temp_txt = ""
        ty += 20
        txtw = 0 

    
    
    

def mousePressed():
    global hold_txt, post_txt, temp_txt, posts
    
    print("Hold: " + str(hold_txt))
    print("Temp: " + str(temp_txt))
    print("Post: " + str(post_txt))

    if mouseButton == LEFT and enter_btn[4]:
        if len(hold_txt) == 0 and temp_txt == "":
            pass
        else:
            hold_txt.append(temp_txt)
            post_txt = "".join(hold_txt)
            temp_txt = ""
            hold_txt = []
            new_post = postFunction(str(len(posts) + 1), users[len(posts) % len(users)], post_txt)
            posts.append(new_post)
            post_txt = ""

        postFunction(0, "", "").convert_post_to_json(posts)
        
# saves line history
# posts multiples posts
# add title
        
