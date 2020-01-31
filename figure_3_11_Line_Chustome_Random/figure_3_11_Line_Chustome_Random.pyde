def setup():
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)
    
    global step, last, pos, border
    step = PVector(10, 10)
    last = PVector(0, height/2)
    pos = PVector(10,height/2)
    border = PVector(20,10)  
    

    
def draw():
    background(255)
    strokeWeight(5)
    global step, last, pos, border

    for pos.x in range(int(pos.x), width, int(step.x)):
        aRand = aRandom()
        pos.y = height/2 + 20 + aRandom() * 80
        line(last.x, last.y, pos.x, pos.y)
        last.x = pos.x
        last.y = pos.y
        
    noLoop()
   
def keyPressed():
    if key == "p":
        print("p Pressed")
        saveFrame("screen-####.png")
             
def aRandom():
    randomNumber = 1
    exponent = 7
    num = 1 - pow(random(randomNumber), exponent)
    
    return num
