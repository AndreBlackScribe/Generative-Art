startNoise =  PVector(random(10), random(10))
posNoise = PVector(startNoise.x, startNoise.y)

def setup():
    global startNoise, posNoise
    
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)
    

def draw():
    for y in xrange(0, height ,5):
        posNoise.y += 0.1
        posNoise.x = startNoise.x
        for x in xrange(0, width, 5):
            posNoise.x += 0.1
            drawLine(x,y, noise(posNoise.x, posNoise.y))
            
  
        noLoop()
        
def drawPoint(x, y, noiseFactor):
    leng = 10 * noiseFactor
    rect(x,y,leng,leng)
    
def drawLine(x, y, noiseFactor):
    pushMatrix()
    translate(x, y)
    rotate(noiseFactor * radians(360) )
    stroke(0,150)
    line(0, 0, 20, 0)
    popMatrix()
