import json
from user import UserObject

username = ""
password = ""
userBoxSelected = False
passBoxSelected = False
userLoggedIn = False

banned_keys = [" ", ",", "."]

usernameError = False
passwordError = False

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
        
        if usernameError:
            fill(255, 0, 0)
            textSize(15)
            text("Username must be between 1-8 characters!", 500, 325)
            fill(0)
            textSize(20)
        
        if passwordError:
            fill(255, 0, 0)
            textSize(15)
            text("Password must be between 5-10 characters!", 500, 425)
            fill(0)
            textSize(20)
        
        if userBoxSelected:
            stroke(0, 0, 255)
            strokeWeight(3)
            fill(255)
            rectMode(CENTER)
            rect(600, 295, 200, 30)
            fill(0)
            stroke(0)
            strokeWeight(1)
        
        fill(0)
        text("Password: ", 400, 400)
        fill(255)
        rect(600, 395, 200, 30)
        
        if passBoxSelected:
            stroke(0, 0, 255)
            strokeWeight(3)
            fill(255)
            rect(600, 395, 200, 30)
            stroke(0)
            strokeWeight(1)
            
        xusername = 510
        
        for letter in username:
            
            fill(0)
            text(letter, xusername, 300)
            xusername += 10
            
        xpassword = 510
        for letter in password:
            
            fill(0)
            textSize(80)
            text(".", xpassword, 400)
            textSize(20)
            xpassword += 15
            
def signOut():
    userLoggedIn = False

def keyPressed():
    global username, password, userLoggedIn, usernameError, passwordError

    if key == BACKSPACE and userBoxSelected:
        username = username[:-1]
    elif key == BACKSPACE and passBoxSelected:
        password = password[:-1]
    elif userBoxSelected and len(username) < 8:
        if key not in banned_keys:
            username += key
    elif passBoxSelected and len(password) < 10:
        if key not in banned_keys:
            password += key
        
    if key == ENTER and len(username) > 0 and len(password) > 5:        
        new_psswd = ""
        for i in pass_str:
            new_psswd += str(ord(i))
        userInfo = UserObject(username, password)
        userInfo.convert_to_json(new_psswd)
        userLoggedIn = True
    elif key == ENTER and len(username) <= 0:
        usernameError = True
        print("Username must be between 1-8 characters!")
    elif key == ENTER and len(password) <= 5:
        passwordError = True
        print("Password must be between 5-10 characters!")
        print(new_psswd)
        
        
def mousePressed():
    global userBoxSelected, passBoxSelected
    if dist(mouseX, mouseY, 600, 295) <= 100:
        passBoxSelected = False
        userBoxSelected = True
    
    elif dist(mouseX, mouseY, 600, 395) <= 100:
        userBoxSelected = False
        passBoxSelected = True
    

    
