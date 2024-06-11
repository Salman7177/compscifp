import json
from user import UserObject

username = []
password = []
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
    if userBoxSelected and len(username) < 8:
        username.append(key)
    elif passBoxSelected and len(password) < 10:
        password.append(key)
        
    if key == ENTER:
        user_str = ''.join(username)
        pass_str = ''.join(password)
        
        userInfo = UserObject(user_str, pass_str)
        userInfo.convert_to_json()
        userInfo.hash_password()
        userLoggedIn = True
        
        
def mousePressed():
    global userBoxSelected, passBoxSelected
    if dist(mouseX, mouseY, 600, 295) <= 100:
        passBoxSelected = False
        userBoxSelected = True
    
    elif dist(mouseX, mouseY, 600, 395) <= 100:
        userBoxSelected = False
        passBoxSelected = True
    

    
