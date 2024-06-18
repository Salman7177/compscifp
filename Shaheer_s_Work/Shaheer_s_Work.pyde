import json



# create buttons
button_nav_home = [0, 0, 250, 100, False]
button_nav_search = [0, 100, 250, 100, False]
button_nav_profile = [0, 620, 250, 100, False]
button_logout = [0, 520, 250, 100, False]
button_edit_bio = [410, 100, 130, 30, False]
button_submit_bio = [550, 100, 130, 30, False]

bio = "BIO IBOIBOIOBI OI BOIBO IBOIBOIB OBIoBIBIOIBOoIB oB ib"
edit_bio = False



# setup script (runs once)
def setup():
    size(1280, 720)
    frameRate(60)






# update loop
def draw():
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
    
    
    # search btn
    if button_nav_search[4]:
        fill(50)
    else:
        fill(30)
    rect(button_nav_search[0], button_nav_search[1], button_nav_search[2], button_nav_search[3])
    fill(255)
    textAlign(LEFT, CENTER)
    textSize(32)
    text("Search", 80, 150)
    search_icon = loadImage("search.png")
    image(search_icon, 50, 150, 30, 30)
    
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
    
    
    fill(0)
    text(str(mouseX) + "," + str(mouseY), width / 2, 700)









def mouse_over_button_logic():
    global button_nav_home, button_nav_search, button_nav_profile
    
    button_nav_home[4] = mouseX > button_nav_home[0] and mouseX < button_nav_home[0] + button_nav_home[2] and mouseY > button_nav_home[1] and mouseY < button_nav_home[1] + button_nav_home[3]
    button_nav_search[4] = mouseX > button_nav_search[0] and mouseX < button_nav_search[0] + button_nav_search[2] and mouseY > button_nav_search[1] and mouseY < button_nav_search[1] + button_nav_search[3]
    button_nav_profile[4] = mouseX > button_nav_profile[0] and mouseX < button_nav_profile[0] + button_nav_profile[2] and mouseY > button_nav_profile[1] and mouseY < button_nav_profile[1] + button_nav_profile[3]
    button_edit_bio[4] = mouseX > button_edit_bio[0] and mouseX < button_edit_bio[0] + button_edit_bio[2] and mouseY > button_edit_bio[1] and mouseY < button_edit_bio[1] + button_edit_bio[3]
    button_submit_bio[4] = mouseX > button_submit_bio[0] and mouseX < button_submit_bio[0] + button_submit_bio[2] and mouseY > button_submit_bio[1] and mouseY < button_submit_bio[1] + button_submit_bio[3]
    button_logout[4] = mouseX > button_logout[0] and mouseX < button_logout[0] + button_logout[2] and mouseY > button_logout[1] and mouseY < button_logout[1] + button_logout[3]

def mousePressed():
    global edit_bio, bio
    if button_edit_bio[4]:
        edit_bio = True
        bio = ""
        
    if button_submit_bio[4]:
        edit_bio = False
        write_bio_to_json()



# key pressed function, handles keyboard input
def keyPressed():
    global bio, edit_bio
    if edit_bio:
        if key == BACKSPACE:
            bio = bio[:-1]
        else:
            if len(bio) < 50:
                bio += key
                
                
def write_bio_to_json():
    
    fp = "data/bio.json"
    file_json = open(fp)
    crue = json.load(file_json)
    crue_2nd = crue["users"]
       
    crue_2nd.append({
        "bio": "hiiiiii"
        })
    user_dict = {"users":crue_2nd}        
    
    with open(fp, "w") as file_json:
        json.dump(user_dict, file_json, ensure_ascii=False, indent=4)
        file_json.write("\n")
    
    
    
