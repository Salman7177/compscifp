import json
from user import UserObject
from post import postFunction
from bio import bioFunction
from postobject import post_object
from scrollbar import Scrollbar

# user variables
username = ""
password = ""
userBoxSelected = False
passBoxSelected = False
userLoggedIn = False
banned_keys = [" ", ",", ".", ENTER]
usernameError = False
passwordError = False

# post variables
users = ["Salman", "Damien", "David", "Shaheer"]
post_txt = ""
new_post = ""
title_txt = ""
temp_txt = ""
hold_txt = []
ty = 20
txtw = 0

# post drawing variables
posts = []
bar = []
scroll_pos = 0

enter_btn = [1185, 150, 90, 35, False]
title_section = [300, 0, 300, 30, False]
text_section = [300, 40, 980, 150, False]

grey = color(54,54,54)

typing_title = False

# create buttons
button_nav_home = [0, 0, 250, 100, False]
button_nav_post = [0, 100, 250, 100, False]
button_nav_profile = [0, 620, 250, 100, False]
button_logout = [0, 520, 250, 100, False]
button_edit_bio = [410, 100, 130, 30, False]
button_submit_bio = [550, 100, 130, 30, False]

bio = ""
edit_bio = False

showHomeScreen = False
showProfileScreen = False
showUserScreen = True
showPostScreen = False
showAllPosts = False



def setup():
    size(1280, 720)
    noStroke()
    global txtw, temp_txt
    txtw = 0
    temp_txt = ""
    noStroke()

def draw():
    background(240)
    
    if showUserScreen:
        userUI()
    
    elif showProfileScreen:
        background(255)
        draw_posts()
        bioUI()
        
        
    

def postMOB():
    global enter_btn, title_section, text_section

    enter_btn[4] = mouseX > enter_btn[0] and mouseX < enter_btn[0] + enter_btn[2] and mouseY > enter_btn[1] and mouseY < enter_btn[1] + enter_btn[3]
    title_section[4] = mouseX > title_section[0] and mouseX < title_section[0] + title_section[2] and mouseY > title_section[1] and mouseY < title_section[1] + title_section[3]
    text_section[4] = mouseX > text_section[0] and mouseX < text_section[0] + text_section[2] and mouseY > text_section[1] and mouseY < text_section[1] + text_section[3]
    
def navMOB():
    global button_nav_home, button_nav_post, button_nav_profile
    button_nav_home[4] = mouseX > button_nav_home[0] and mouseX < button_nav_home[0] + button_nav_home[2] and mouseY > button_nav_home[1] and mouseY < button_nav_home[1] + button_nav_home[3]
    button_nav_post[4] = mouseX > button_nav_post[0] and mouseX < button_nav_post[0] + button_nav_post[2] and mouseY > button_nav_post[1] and mouseY < button_nav_post[1] + button_nav_post[3]
    button_nav_profile[4] = mouseX > button_nav_profile[0] and mouseX < button_nav_profile[0] + button_nav_profile[2] and mouseY > button_nav_profile[1] and mouseY < button_nav_profile[1] + button_nav_profile[3]
    
def bioMOB():
    global button_edit_bio, button_submit_bio, button_logout
    button_edit_bio[4] = mouseX > button_edit_bio[0] and mouseX < button_edit_bio[0] + button_edit_bio[2] and mouseY > button_edit_bio[1] and mouseY < button_edit_bio[1] + button_edit_bio[3]
    button_submit_bio[4] = mouseX > button_submit_bio[0] and mouseX < button_submit_bio[0] + button_submit_bio[2] and mouseY > button_submit_bio[1] and mouseY < button_submit_bio[1] + button_submit_bio[3]
    button_logout[4] = mouseX > button_logout[0] and mouseX < button_logout[0] + button_logout[2] and mouseY > button_logout[1] and mouseY < button_logout[1] + button_logout[3]

def bioUI():
    
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
    
    # post btn
    if button_nav_post[4]:
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
    text(username, 80, 720 - 50)
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
        
    bioMOB()
    navMOB()
        
def postUI():
    global temp_txt, title_txt, tx, ty
    rectMode(CORNER)
    # if text_section or title_section:
    #     cursor(TEXT)
    # else:
    #     cursor(POINT)
    
    # Title Text Box
    if typing_title:
        fill(200)
        stroke(14,51,23)
    else:
        noStroke()
        fill(230)
    rect(title_section[0], title_section[1], title_section[2], title_section[3])
    fill(0)
    text("Title: ", 305, 15)
    text(title_txt, 340, 15)
    noStroke()
    
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

def userUI():
    global username
    background(240)
    
    textSize(20)
    
    fill(0)
    text("Social Media Site", 620, 40)
    
    # Form
    fill(0)
    text("Username: " , 400, 300)
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
        noStroke()
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
        noStroke()
        strokeWeight(1)
            
    xusername = 510
    fill(0)
    text(username, 505, 302)

    xpassword = 500
    for letter in password:
        fill(0)
        textSize(80)
        text(".", xpassword, 400)
        textSize(20)
        xpassword += 15

    rectMode(CORNER)
def userTypingFunction():
    global username, password, userLoggedIn, usernameError, passwordError, showProfileScreen, showUserScreen

    if keyCode == SHIFT:
        pass
    elif key == BACKSPACE and userBoxSelected:
        username = username[:-1]
    elif key == BACKSPACE and passBoxSelected:
        password = password[:-1]
    elif userBoxSelected and len(username) < 18:
        if key not in banned_keys:
            username += key
    elif passBoxSelected and len(password) < 10:
        if key not in banned_keys:
            password += key
        
    # if key == ENTER and (len(username) > 0 and len(password) > 5):        
    #     new_psswd = ""
    #     for i in password:
    #         new_psswd += str(ord(i))
    #     userInfo = UserObject(username, password)
    #     userInfo.convert_to_json(new_psswd)
    #     userLoggedIn = True
    #     showProfileScreen = True
    #     showUserScreen = False
    #     import_posts(False)
    #     print(showUserScreen)

    if key == ENTER and (len(username) > 0 and len(password) > 5):        
        new_psswd = [ord(c) for c in password]
        json_psswd = ''.join(map(str, new_psswd))
        
        
        unhashed_psswd = [chr(c) for c in new_psswd]
        unhashed_psswd = ''.join(unhashed_psswd)
        


        with open("data/users-info.json") as raw_json_file:
            
            data = json.load(raw_json_file)
            for a in data['users']:
                if a['username'] == username and unhashed_psswd == a['password']:
                     
                    print('found EXACT username and password match')
                    
                elif a['username'] == username:
                    usernameError = 'Username already exists or you entered the wrong password!'
        
        
        userInfo = UserObject(username, password)
        userInfo.convert_to_json(json_psswd)
        userLoggedIn = True
        showProfileScreen = True
        showUserScreen = False
        import_posts(False)

    elif key == ENTER and len(username) <= 0:
        usernameError = True
        print("Username must be between 1-8 characters!")
    elif key == ENTER and len(password) <= 5:
        passwordError = True
        print("Password must be between 5-10 characters!")




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
                new_post = postFunction(int(round(random(0,1000),0)), username, title_txt, post_txt)
                post_txt = ""
                title_txt = ""
                
            ty = 20
            postFunction(0, "", "", "").convert_post_to_json(new_post)
            print("h")

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

def bioTypingFunction():
    global bio, edit_bio
    if edit_bio:
        if keyCode == SHIFT:
            pass
        elif key == BACKSPACE:
            bio = bio[:-1]
        else:
            if len(bio) < 50:
                bio += key
                
def bioMouseFunction():
    global edit_bio, bio
    if button_edit_bio[4]:
        edit_bio = True
        bio = ""
        
    if button_submit_bio[4]:
        edit_bio = False
        new_bio = bioFunction(username, bio)

        bioFunction("","").write_bio_to_json(new_bio)   

# Imports all posts once user or profile page is loaded. is_profile determines whether to view posts based on user profile or not
def import_posts(is_profile):
    global posts, max_scroll
    
    file_json = open("posts.json")
    loaded_posts = json.load(file_json)
    for i in loaded_posts["posts"]:
        if is_profile == True:
            if i["user"] == username:
                cur_post = post_object(i["user"], i["title"], i["post_txt"])
                posts.insert(0, cur_post)
        else:
            cur_post = post_object(i["user"], i["title"], i["post_txt"])
            posts.insert(0, cur_post)
    print(len(posts))
    max_scroll = (len(posts) * -200) + height - 150 # Max scroll should add up all the heights of each individual post box and subtract the height to make sure it ends at the last post.
    bar.append(Scrollbar(len(posts), scroll_pos, max_scroll))

def draw_posts():
    global posts
    num_posts = 0
    for i in posts:
        i.y = (200 * num_posts) + scroll_pos + 150
        i.draw_posts()
        num_posts += 1
    for i in bar:
        i.scroll_pos = scroll_pos
        i.display()

def page_state():
    if mouseButton == LEFT and button_nav_home[4]:
        showHomeScreen = True
        import_posts(False)

def keyPressed():
    if showUserScreen:
        userTypingFunction()
    elif showPostScreen:
        postTypingFunction()
    elif showProfileScreen:
        bioTypingFunction()
        
def mousePressed():
    if showUserScreen:
        userMouseFunction()
    elif showPostScreen:
        postMouseFunction()
    elif showProfileScreen:
        bioMouseFunction()
        
# mousewheel scrolling script, if we ever do multiple scrollbars make sure that the user is selected or hovering over the element they want to scroll over.    
def mouseWheel(event):
    global scroll_pos, posts, max_scroll
    
    print(max_scroll)
    if max_scroll < 0:
        scroll_pos -= event.getCount() * 25
        if scroll_pos > 0:
            scroll_pos = 0
        elif scroll_pos < max_scroll:
            scroll_pos = max_scroll
