radius = 10
pos = PVector()
lastPos = PVector(-999, -999)
randNoise = random(10.0)

def setup():
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)
    
    
def draw():
    global radius, randNoise, lastPos
    stroke(20,50,70)
    pos = PVector(width/2, height/2)
    
    for angle in range(0, 1440, 5):
        rad = radians(angle)
        radius = angle / 10
        
        randNoise += 0.05
        noisyRadius = radius + (noise(randNoise)*100) - 100
        
        lastPos = pos.copy()
        pos.x = width/2  + (noisyRadius * cos(rad))
        pos.y = height/2 + (noisyRadius * sin(rad))
        if lastPos.x > -999:
            point(pos.x, pos.y)
            #line(pos.x, pos.y, lastPos.x, lastPos.y)
        
        noLoop()
