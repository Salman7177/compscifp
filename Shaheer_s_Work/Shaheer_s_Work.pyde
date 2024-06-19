import json
from bio import bioFunction

# create buttons
button_nav_home = [0, 0, 250, 100, False]
button_nav_post = [0, 100, 250, 100, False]
button_nav_profile = [0, 620, 250, 100, False]
button_logout = [0, 520, 250, 100, False]
button_edit_bio = [410, 100, 130, 30, False]
button_submit_bio = [550, 100, 130, 30, False]

bio = ""
edit_bio = False
username = "Salman"

# setup script (runs once)
def setup():
    size(1280, 720)
    frameRate(60)






# update loop
def draw():
    pass

def bioUserInterface():
    background(255)
    
    # draw profile page
    fill(30)
    stroke(125)
    rect(0, 0, 250, height)
    rect(250, 0, 1280 - 250, 150)
    
    #navbar
    # home btn
    if button_nav_home[4]:
        fill(50)
    else:
        fill(30)
    rect(button_nav_home[0], button_nav_home[1], button_nav_home[2], button_nav_home[3])
    fill(255)
    textAlign(LEFT, CENTER)
    textSize(32)
    text("Home", 80, 50)
    home_icon = loadImage("home.png")
    imageMode(CENTER)
    image(home_icon, 50, 50, 30, 30)
    
<<<<<<< HEAD
<<<<<<< HEAD
    # search btn
    if button_nav_search[4]:
=======
    
    # post btn
    if button_nav_post[4]:
>>>>>>> 778e84fd388570faedc4af352f46630e99833a43
=======
    
    # post btn
    if button_nav_post[4]:
>>>>>>> 778e84fd388570faedc4af352f46630e99833a43
        fill(50)
    else:
        fill(30)
    rect(button_nav_post[0], button_nav_post[1], button_nav_post[2], button_nav_post[3])
    fill(255)
    textAlign(LEFT, CENTER)
    textSize(32)
    text("Post", 80, 150)
    post_icon = loadImage("post.png")
    image(post_icon, 50, 150, 30, 30)
    
    # profile btn
    if button_nav_profile[4]:
        fill(50)
    else:
        fill(30)    
    rect(button_nav_profile[0], button_nav_profile[1], button_nav_profile[2], button_nav_profile[3])
    fill(255)
    textAlign(LEFT, CENTER)
    textSize(32)
    text("Username", 80, 720 - 50)
    profile_icon = loadImage("profile.png")
    image(profile_icon, 50, 720 - 50, 50, 50)
    
    #logout button
    if button_logout[4]:
        fill(50)
    else:
        fill(30)    
    rect(button_logout[0], button_logout[1], button_logout[2], button_logout[3])
    fill(255)
    textAlign(LEFT, CENTER)
    textSize(32)
    text("Logout", 80, 720 - 150)
    logout_icon = loadImage("logout.png")
    image(logout_icon, 50, 720 - 150, 50, 50)
    
    # top bar
    image(profile_icon, 350, 80, 100, 100)
    fill(255)
    text("USERNAME", 410, 50)
    textSize(20)
    text(bio, 410, 80)
    
    #edit bio button
    if button_edit_bio[4]:
        fill(180)
    else:
        fill(220)  
    rect(button_edit_bio[0], button_edit_bio[1], button_edit_bio[2], button_edit_bio[3])
    fill(0)
    text("Retype Bio", 425, 115)
    
    if edit_bio:
        if button_edit_bio[4]:
            fill(180)
        else:
            fill(220) 
        rect(button_submit_bio[0], button_submit_bio[1], button_submit_bio[2], button_submit_bio[3])
        fill(0)
        text("Submit", 555, 115)
    
    mouse_over_button_logic()
<<<<<<< HEAD
=======
    
    







>>>>>>> 778e84fd388570faedc4af352f46630e99833a43

def mouse_over_button_logic():
    global button_nav_home, button_nav_post, button_nav_profile
    
    button_nav_home[4] = mouseX > button_nav_home[0] and mouseX < button_nav_home[0] + button_nav_home[2] and mouseY > button_nav_home[1] and mouseY < button_nav_home[1] + button_nav_home[3]
    button_nav_post[4] = mouseX > button_nav_post[0] and mouseX < button_nav_post[0] + button_nav_post[2] and mouseY > button_nav_post[1] and mouseY < button_nav_post[1] + button_nav_post[3]
    button_nav_profile[4] = mouseX > button_nav_profile[0] and mouseX < button_nav_profile[0] + button_nav_profile[2] and mouseY > button_nav_profile[1] and mouseY < button_nav_profile[1] + button_nav_profile[3]
    button_edit_bio[4] = mouseX > button_edit_bio[0] and mouseX < button_edit_bio[0] + button_edit_bio[2] and mouseY > button_edit_bio[1] and mouseY < button_edit_bio[1] + button_edit_bio[3]
    button_submit_bio[4] = mouseX > button_submit_bio[0] and mouseX < button_submit_bio[0] + button_submit_bio[2] and mouseY > button_submit_bio[1] and mouseY < button_submit_bio[1] + button_submit_bio[3]
    button_logout[4] = mouseX > button_logout[0] and mouseX < button_logout[0] + button_logout[2] and mouseY > button_logout[1] and mouseY < button_logout[1] + button_logout[3]



def bioMouseFunction():
    global edit_bio, bio
    if button_edit_bio[4]:
        edit_bio = True
        bio = ""
        
    if button_submit_bio[4]:
        edit_bio = False
        new_bio = bioFunction(username, bio)

        bioFunction("","").write_bio_to_json(new_bio)

def mousePressed():
    bioMouseFunction()

def bioKeyboardFunction():
    global bio, edit_bio
    if edit_bio:
        if keyCode == SHIFT:
            pass
        elif key == BACKSPACE:
            bio = bio[:-1]
        else:
            if len(bio) < 50:
                bio += key
                

# key pressed function, handles keyboard input
def keyPressed():
    bioKeyboardFunction()
                
    
    
    
