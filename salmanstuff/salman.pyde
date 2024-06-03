import json

def setup():
    size(1280, 720)
    background(240)
    noStroke()

posttxt = ["Hello", "Monkey", "Black", "Grape"]
users = ["Salman", "Damien", "David", "Shaheer"]

temp_txt = ""

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
    
    # Text Box
    fill(255)
    rect(300, 0, width - 300, 150)
    
    # Display typed text
    fill(0)
    textSize(15)
    
    x = 310
    y = 20
    txtw = textWidth(temp_txt)
    print(txtw)
    if txtw < 960:
        text(temp_txt, x, y)
    elif txt > 960:
        x = 310
        y += 20
    
    
    

    

def keyPressed():
    global posttxt
    global temp_txt
    
    if key == BACKSPACE:
        temp_txt = temp_txt[:-1]
    elif key == ENTER:
        posttxt.append(temp_txt)
        print(posttxt)

    elif keyCode == SHIFT:
        pass
    else:
        temp_txt += key
    
