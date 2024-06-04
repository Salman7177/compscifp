import json

posttxt = ["Hello", "Monkey", "Black", "Grape"]
users = ["Salman", "Damien", "David", "Shaheer"]

temp_txt = ""
txt_hold = []
tx, ty = 310, 20
txtw = 0

def setup():
    size(1280, 720)
    global txtw, temp_txt, tx, ty
    txtw = 0
    temp_txt = ""
    tx, ty = 310, 20

def draw():
    background(200) 
    UserInterface()

def UserInterface():
    global temp_txt
    global tx, ty

    # Text Box
    fill(255)
    rect(300, 0, width - 300, 150)

    # Display typed text
    fill(0)
    textSize(15)
    
    # Display the held lines
    for i, line in enumerate(txt_hold):
        text(line, 310, 20 + i * 20)
    
    # Display the current typing line
    text(temp_txt, 310, ty)

def keyPressed():
    global posttxt
    global temp_txt
    global txt_hold
    global ty
    global txtw

    if keyCode == SHIFT:
        pass
    elif key == BACKSPACE:
        if len(temp_txt) > 0:
            temp_txt = temp_txt[:-1]
        elif len(txt_hold) > 0:
            temp_txt = txt_hold.pop() + temp_txt
            ty -= 20
    elif key == ENTER:
        txt_hold.append(temp_txt)
        temp_txt = ""
        ty += 20
    else:
        temp_txt += key

    txtw = textWidth(temp_txt)
    if txtw > 960:
        txt_hold.append(temp_txt)
        temp_txt = ""
        ty += 20
        txtw = 0 

    print(txt_hold)
