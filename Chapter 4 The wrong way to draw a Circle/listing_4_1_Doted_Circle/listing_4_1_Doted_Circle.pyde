radius = 100
pos = PVector()

def setup():
    size(1024,1024,P2D)
    frameRate(30)
    smooth(8)
    background(255)
    
    
def draw():
    stroke(20,50,70)
    for angle in range(0, 360, 5):
        rad = radians(angle)
        
        pos.x = width/2  + (radius * cos(rad))
        pos.y = height/2 + (radius * sin(rad))
        point(pos.x, pos.y)
