import json
from post import postFunction

users = ["Salman", "Damien", "David", "Shaheer"]
post_txt = ""
new_post = ""
title_txt = ""
temp_txt = ""
hold_txt = []
ty = 70
txtw = 0

enter_btn = [1185, 150, 90, 35, False]
title_section = [300, 0, 300, 30, False]
text_section = [300, 40, 980, 150, False]

grey = [54, 54, 54]

typing_title = False



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
    title_section[4] = mouseX > title_section[0] and mouseX < title_section[0] + title_section[2] and mouseY > title_section[1] and mouseY < title_section[1] + title_section[3]
    text_section[4] = mouseX > text_section[0] and mouseX < text_section[0] + text_section[2] and mouseY > text_section[1] and mouseY < text_section[1] + text_section[3]
    
    
    
    
    
    
    

def UserInterface():
    global temp_txt, title_txt, tx, ty

    # Title Text Box
    fill(230)
    rect(title_section[0], title_section[1], title_section[2], title_section[3])
    fill(0)
    text("Title: ", 305, 15)
    text(title_txt, 340, 15)
    
    # Post Text Box
    fill(255)
    rect(300, 40, width - 300, 150)
    
    # Display typed text
    fill(0)
    textSize(15)
    
    # Display the held lines
    for i, line in enumerate(hold_txt):
        text(line, 310, 60 + i * 20)
    
    # Display the current typing line
    text(temp_txt, 310, ty+40)
    
    # Enter button
    if enter_btn[4]:
        fill(125,0,0)
    else:
        fill(grey[0], grey[1], grey[2])
    rect(enter_btn[0], enter_btn[1], enter_btn[2], enter_btn[3])
    
    fill(255)
    textAlign(CORNER, CENTER)
    text("Post", 1217, 167)
    textAlign(CORNER, CENTER)
    
    
    
    
def keyPressed():
    global post_txt, temp_txt, hold_txt, ty, txtw, title_txt
    
    if keyCode == SHIFT:
        pass
    elif key == BACKSPACE:
        if typing_title:
            if len(title_txt) > 0:
                title_txt = title_txt[:-1]
        else:
            if len(temp_txt) > 0:
                temp_txt = temp_txt[:-1]
            elif len(hold_txt) > 0:
                temp_txt = hold_txt.pop() + temp_txt
                ty -= 20
    elif key == ENTER:
        if len(hold_txt) < 4:
            hold_txt.append(temp_txt)
            temp_txt = ""
            ty += 20
    else:
        if typing_title:
            if textWidth(title_txt + key) <= 500:
                title_txt += key
        else:
            temp_txt += key

    txtw = textWidth(temp_txt)
    if txtw > 960:
        hold_txt.append(temp_txt)
        temp_txt = ""
        ty += 20
        txtw = 0 





def mousePressed():
    global hold_txt, post_txt, temp_txt, title_txt, typing_title, ty, new_post
    

    if mouseButton == LEFT:
        if title_section[4]:
            typing_title = True
        elif text_section[4]:
            typing_title = False

        if enter_btn[4]:
            if len(hold_txt) == 0 and temp_txt == "" and title_txt == "":
                pass
            else:
                hold_txt.append(temp_txt)
                post_txt = "|".join(hold_txt)
                temp_txt = ""
                hold_txt = []
                new_post = postFunction(random(0,1000), users[int(random(0,3))], title_txt, post_txt)
                post_txt = ""
                title_txt = ""
                
            ty = 20
            postFunction(0, "", "", "").convert_post_to_json(new_post)
