def setup():
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)
    
    global step, last, pos, border, angle
    step = PVector(10, 10)
    last = PVector(0, height/2)
    pos = PVector(10,height/2)
    border = PVector(20,10)
    angle = 0
    

    
def draw():
    strokeWeight(5)
    global step, last, pos, border, angle

    for pos.x in range(int(pos.x), width, int(step.x)):
        #func = height/2 +  sin(radians(angle)) * 100 #Sine
        #func = height/2 +  pow(sin(radians(angle)),3) * 100 #Cubic Sine
        func = height/2 +  sin(radians(angle)) * noise(radians(angle))  * 100 #Sine withn Noise
        pos.y = func
        
        line(last.x, last.y, pos.x, pos.y)
        
        last.x = pos.x
        last.y = pos.y
        angle += 10
        
    last = PVector(0, height/2)
    pos = PVector(10,height/2)
    angle = 0
    
    
    
   
def keyPressed():
    if key == "p":
        print("p Pressed")
        saveFrame("screen-####.png")     
    
