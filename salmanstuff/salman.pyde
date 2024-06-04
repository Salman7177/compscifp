import json

def setup():
    size(1280, 720)
    background(240)
    noStroke()

posttxt = ["Hello", "Monkey", "Black", "Grape"]
users = ["Salman", "Damien", "David", "Shaheer"]

temp_txt = ""
txt_hold = []
txtw = textWidth(temp_txt)
tx = 310
ty = 20

def draw():
    # savePostsToJson()
    
    UserInterface()

# def savePostsToJson():
#     global posts, posttxt, users
#     posts = []
    
#     for i in range(len(posttxt)):
#         post = {
#             "id": i,
#             "user": users[i % len(users)],
#             "post-txt": posttxt[i]
#         }
#         posts.append(post)
    
#     saveJSONArray(posts, "data/new.json")

def UserInterface():
    global temp_txt
    global tx, ty
    
    # Text Box
    fill(255)
    rect(300, 0, width - 300, 150)
    
    # Display typed text
    fill(0)
    textSize(15)
    
    print(txtw)
    text(temp_txt, 310, ty)


def keyPressed():
    global posttxt
    global temp_txt
    global txt_hold
    global ty
    

        
    if keyCode == SHIFT:
        pass
    elif key == BACKSPACE:
        temp_txt = temp_txt[:-1]
    elif key == ENTER:
        # Combine the hold list into one string the appended it posttxt
        pass
    elif txtw > 960:
        txt_hold.append(temp_txt)
        temp_txt = ""
        ty += 10
    else:
        temp_txt += key
        
    txtw = textWidth(temp_txt)
# Put all the typed code into a string
# when the temp text width is bigger then 960 appended it to holding list
# set the txt y + 20
    
