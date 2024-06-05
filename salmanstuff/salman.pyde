import json

posttxt = ["Hello", "Monkey", "Black", "Grape"]
users = ["Salman", "Damien", "David", "Shaheer"]

temp_txt = ""
txt_hold = []
tx, ty = 310, 20
txtw = 0

enter_btn = [1185, 110, 90, 35, False]

grey = [54, 54, 54]

def setup():
    size(1280, 720)
    global txtw, temp_txt, tx, ty
    txtw = 0
    temp_txt = ""
    tx, ty = 310, 20
    noStroke()

def draw():
    background(240) 
    UserInterface()
    
    fill(0)
    textAlign(CENTER, CENTER)
    text(str(mouseX) + ", " + str(mouseY), width/2, height-10)
    textAlign(CORNER, CENTER)
    
    mouse_over_button_logic()
    
def mouse_over_button_logic():
    global enter_btn
    
    enter_btn[4] = mouseX > enter_btn[0] and mouseX < enter_btn[0] + enter_btn[2] and mouseY > enter_btn[1] and mouseY < enter_btn[1] + enter_btn[3]


    
    
    
    
    
    
    

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
    
    # Enter button
    fill(grey[0], grey[1], grey[2])
    rect(enter_btn[0], enter_btn[1], enter_btn[2], enter_btn[3])
    
    fill(255)
    textAlign(CORNER, CENTER)
    text("Post", 1217, 127)
    textAlign(CORNER, CENTER)
    
    
    
    

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
        if len(txt_hold) < 5:  # Check if less than 5 lines are already present
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

    
    
    
    
def mousePressed():
    global txt_hold, posttxt, temp_txt
    
    if mouseButton == LEFT and enter_btn[4]:
        txt_hold.append(temp_txt)
        posttxt = "".join(txt_hold)  # Join txt_hold into a single string
        print(str(posttxt))
