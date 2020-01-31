radius = 100
pos = PVector()
lastPos = PVector(-999, -999)
randNoise = random(10.0)
drawLoops = 0

def setup():
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)
    

    
def draw():
    global radius, randNoise, lastPos, drawLoops
    drawLoops += 1
    pos = PVector(width/2, height/2)
    
    stroke(0, 30)
    noFill()
    ellipse(width/2, height/2, radius*2, radius*2)
    
    stroke(20,50,70)
    strokeWeight(1)
    
    noiseVal = random(10.0)
    
    beginShape()
    fill(20, 50, 70, 50)
    
   
    
    for angle in range(0, 360, 1):
        noiseVal += 0.1
        radVariance = 30 * customNoise(noiseVal)
        
        noisyRadius = radius + radVariance
        rad = radians(angle)
        
        pos.x = width/2  + (noisyRadius * cos(rad))
        pos.y = height/2 + (noisyRadius * sin(rad))
        
        
        curveVertex(pos.x, pos.y)
    
    endShape()
        

        
    if drawLoops >= 1:
            noLoop()
         
            
               
                     
            
def customNoise(value):
    #return pow(sin(float(value)), int(value % 12)) # Looks like inner rings of a tree
    return pow(sin(float(value)),3)
