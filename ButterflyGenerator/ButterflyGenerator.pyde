yoff=0

def setup():
    size(400, 400)
    
def draw():
    global yoff
    background(51)
    translate(width/2, height/2)
    stroke(255)
    rotate(PI/2)
    
    da = PI/250
    dx=0.2
    r = 100
    angle=-PI/2+(0.01)
    beginShape()
    fill(255, 50)
    xoff=0
    while angle<=(3*PI/2):
        r = sin(2*angle) * map(noise(xoff, yoff), 0, 1, 100, 200)
        x = r * cos(angle)
        y = map(abs(cos(yoff)), 0, 1, 0.5, 1) * r * sin(angle)
        xoff = xoff + dx if angle<=PI/2 else xoff - dx
        angle+=da
        vertex(x, y)
    endShape()
    
    yoff+=0.1
