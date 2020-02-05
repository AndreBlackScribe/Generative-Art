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
        posNoise.y += 0.01
        posNoise.x = startNoise.x
        for x in xrange(0, width, 5):
            posNoise.x += 0.01
            stroke(0, int(noise(posNoise.x, posNoise.y) * 255))
            line(x, y, x+1, y+1)
            
        noLoop()
