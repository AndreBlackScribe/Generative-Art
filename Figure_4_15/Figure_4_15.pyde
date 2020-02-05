angNoise, radNoise = random(10), random(10)
posNoise = PVector(random(10), random(10))
angle = -PI/2
strokeCol = 254
strokeChange = -1

def setup():
    size(1024,1024,P2D)
    #frameRate(30)
    smooth(8)
    background(255)
    noFill()
    
def draw():
    global angNoise, radNoise, angle, strokeCol, strokeChange
    radNoise += 0.005
    radius = (noise(radNoise) * 550 ) + 1
    
    angNoise += 0.005
    angle += (noise(radNoise) * 6 ) - 3  
    
    #if angle > 360: angle -= 360
    #if angle < 0: angle += 360
    angle = angle % 360
    
    posNoise.x += 0.01
    posNoise.y += 0.01
    
    center = PVector( (width/2 + (noise(posNoise.x) * 100) - 50 ), (height/2 + (noise(posNoise.y) * 100) - 50) )
    
    rad = radians(angle)
    pos1 = PVector((center.x+(radius * cos(rad))) , (center.y+(radius * sin(rad)) ))
    
    opprad = rad + PI
    pos2 = PVector((center.x+(radius * cos(opprad))) , (center.y+(radius * sin(opprad)) ))
    
    strokeCol  += strokeChange
    if strokeCol > 254: strokeChange = -1
    if strokeCol < 0: strokeChange = 1
    stroke(strokeCol, 60)
    strokeWeight(1)
    line(pos1.x, pos1.y, pos2.x, pos2.y)
    
