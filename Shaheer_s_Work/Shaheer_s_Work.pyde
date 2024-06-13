
# create buttons
button_nav_home = [0, 0, 250, 100, False]
button_nav_search = [0, 100, 250, 100, False]
button_nav_profile = [0, 620, 250, 100, False]
button_edit_bio = [410, 100, 100, 30, False]

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
    text("Search", 80, 720 - 50)
    profile_icon = loadImage("profile.png")
    image(profile_icon, 50, 720 - 50, 50, 50)
    
    
    
    # top bar
    image(profile_icon, 350, 80, 100, 100)
    fill(255)
    text("USERNAME", 410, 50)
    textSize(20)
    text("bio bio bio bio bio bio boi oib boi obi boi ibo bio bo", 410, 80)
    
    #edit bio button
    if button_edit_bio[4]:
        fill(180)
    else:
        fill(220)  
    rect(button_edit_bio[0], button_edit_bio[1], button_edit_bio[2], button_edit_bio[3])
    fill(0)
    text("Edit Bio", 425, 115)
    
    
    
    mouse_over_button_logic()
    
    
    fill(0)
    text(str(mouseX) + "," + str(mouseY), width / 2, 700)









def mouse_over_button_logic():
    global button_nav_home, button_nav_search, button_nav_profile
    
    button_nav_home[4] = mouseX > button_nav_home[0] and mouseX < button_nav_home[0] + button_nav_home[2] and mouseY > button_nav_home[1] and mouseY < button_nav_home[1] + button_nav_home[3]
    button_nav_search[4] = mouseX > button_nav_search[0] and mouseX < button_nav_search[0] + button_nav_search[2] and mouseY > button_nav_search[1] and mouseY < button_nav_search[1] + button_nav_search[3]
    button_nav_profile[4] = mouseX > button_nav_profile[0] and mouseX < button_nav_profile[0] + button_nav_profile[2] and mouseY > button_nav_profile[1] and mouseY < button_nav_profile[1] + button_nav_profile[3]
    button_edit_bio[4] = mouseX > button_edit_bio[0] and mouseX < button_edit_bio[0] + button_edit_bio[2] and mouseY > button_edit_bio[1] and mouseY < button_edit_bio[1] + button_edit_bio[3]





# key pressed function, handles keyboard input
def keyPressed():
    pass
