drawLoops = 0

def setup():
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)

    
    
def draw():
    global drawLoops
    pos = PVector()
    stroke(20,50,70)
    strokeWeight(0.5)
    pos = PVector(width/2, height/2)
    drawLoops += 1
    
    for number in range(100):
        radius = 10.0
        radNoise = random(10.0)
        lastPos = PVector(-999, -999)
        stroke(random(20), random(50), random(70), 80)
        
        startAngle = int(random(360))
        endAngle = 1440 + int(random(1440))
        stepAngle = 5 + int(random(3))
        
        
        for angle in xrange(startAngle, endAngle, stepAngle):
            radNoise += 0.05
            radius += 0.5
            noisyRadius = radius + (noise(radNoise)*200) - 100
            rad = float(radians(angle))
            
            radius = angle / 10
        

            lastPos = pos.copy()
            pos.x = width/2  + (noisyRadius * cos(rad))
            pos.y = height/2 + (noisyRadius * sin(rad))
            if lastPos.x > -999:
                point(pos.x, pos.y)
                #line(pos.x, pos.y, lastPos.x, lastPos.y)
            
            if drawLoops >= 100:
                noLoop()
