import json
from user import UserObject

# user variables
username = ""
password = ""
userBoxSelected = False
passBoxSelected = False
userLoggedIn = False

# post variables
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

grey = color(54,54,54)

typing_title = False


def setup():
    size(1280, 720)
    noStroke()

def draw():
    if not userLoggedIn:
        postUI()
        mouse_over_button_logic()
    else:
        userUI()
    
def postUI():
    global temp_txt, title_txt, tx, ty

    # if text_section or title_section:
    #     cursor(TEXT)
    # else:
    #     cursor(POINT)
    
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
        fill(grey)
    rect(enter_btn[0], enter_btn[1], enter_btn[2], enter_btn[3])
    
    fill(255)
    textAlign(CORNER, CENTER)
    text("Post", 1217, 167)
    textAlign(CORNER, CENTER)

def mouse_over_button_logic():
    global enter_btn
    
    enter_btn[4] = mouseX > enter_btn[0] and mouseX < enter_btn[0] + enter_btn[2] and mouseY > enter_btn[1] and mouseY < enter_btn[1] + enter_btn[3]
    title_section[4] = mouseX > title_section[0] and mouseX < title_section[0] + title_section[2] and mouseY > title_section[1] and mouseY < title_section[1] + title_section[3]
    text_section[4] = mouseX > text_section[0] and mouseX < text_section[0] + text_section[2] and mouseY > text_section[1] and mouseY < text_section[1] + text_section[3]

def userUI():
    global username
    if userLoggedIn == False:
        background(240)
        
        textSize(20)
        
        fill(0)
        text("Social Media Site", 620, 40)
        
        # Form
        fill(0)
        text("Username: ", 400, 300)
        fill(255)
        rectMode(CENTER)
        rect(600, 295, 200, 30)
        fill(0)
        
        fill(0)
        text("Password: ", 400, 400)
        fill(255)
        rect(600, 395, 200, 30)

        xusername = 510
        fill(0)
        text(username, 505, 30223123)
    
        xpassword = 500
        for letter in password:
            fill(0)
            textSize(80)
            text(".", xpassword, 400)
            textSize(20)
            xpassword += 15

def userTypingFunction():
    global username, password, userLoggedIn

    if key == BACKSPACE and userBoxSelected:
        username = username[:-1]
    elif key == BACKSPACE and passBoxSelected:
        password = password[:-1]
    elif userBoxSelected and len(username) < 18:
        username += key
    elif passBoxSelected and len(password) < 10:
        password += key
        
    if key == ENTER:        
        new_psswd = ""
        for i in pass_str:
            new_psswd += str(ord(i))
        print(new_psswd)
    
        userInfo = UserObject(username, password)
        userInfo.convert_to_json(new_psswd)
        # userInfo.hash_password()
        userLoggedIn = True

def userMouseFunction():
    global userBoxSelected, passBoxSelected
    if dist(mouseX, mouseY, 600, 295) <= 100:
        passBoxSelected = False
        userBoxSelected = True
    
    elif dist(mouseX, mouseY, 600, 395) <= 100:
        userBoxSelected = False
        passBoxSelected = True  
        
def postMouseFunction():
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
                new_post = postFunction(int(round(random(0,1000),0)), users[int(random(0,3))], title_txt, post_txt)
                post_txt = ""
                title_txt = ""
                
            ty = 20
            postFunction(0, "", "", "").convert_post_to_json(new_post)

def postTypingFunction():
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

def keyPressed():
    if not userLoggedIn:
        postTypingFunction()
    else:
        userTypingFunction()
        
def mousePressed():
    if not userLoggedIn:
        postMouseFunction()
    else:
        userMouseFunction()
    

    
