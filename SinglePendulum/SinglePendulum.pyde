origin = bob = l = angle = PI/4
aVel = 0.0
aAcc = 0.0

def setup():
    global l, origin, bob
    size(640, 360)
    l = 180
    origin = PVector(width/2, 0)
    bob = PVector(width/2, l)
    
    
def draw():
    global bob, angle, aAcc, aVel
    background(255)
    bob.x = origin.x + l * sin(angle)
    bob.y = origin.y + l * cos(angle)
    line(origin.x, origin.y, bob.x, bob.y)
    ellipse(bob.x, bob.y, 15, 15)
    
    aAcc = -0.01 * sin(angle)
    angle += aVel
    aVel += aAcc
    
    aVel *= 0.99
