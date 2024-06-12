import json
from user import UserObject

username = ""
password = ""
userBoxSelected = False
passBoxSelected = False
userLoggedIn = False

def setup():
    size(1280, 720)

def draw():
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
        
        for letter in username:
            
            fill(0)
            text(letter, xusername, 300)
            xusername += 10

            
        xpassword = 500
        for letter in password:
            
            fill(0)
            textSize(80)
            text(".", xpassword, 400)
            textSize(20)
            xpassword += 15

def keyPressed():
    global username, password, userLoggedIn

    if key == BACKSPACE and userBoxSelected:
        username = username[:-1]
    elif key == BACKSPACE and passBoxSelected:
        password = password[:-1]
    elif userBoxSelected and len(username) < 8:
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
        
        
def mousePressed():
    global userBoxSelected, passBoxSelected
    if dist(mouseX, mouseY, 600, 295) <= 100:
        passBoxSelected = False
        userBoxSelected = True
    
    elif dist(mouseX, mouseY, 600, 395) <= 100:
        userBoxSelected = False
        passBoxSelected = True
    

    
