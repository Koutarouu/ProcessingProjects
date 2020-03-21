from __future__ import division

n, d = 4, 7


def mouseWheel(event): 
    global n
    if event.count<1:
        n= n + 1 if n<10 else 1
    else:
        n= n - 1 if n>1 else 10

def setup():
    size(500, 500)
    
def draw():
    global d
    k = n/d
    background(51)
    translate(width/2, height/2)
    beginShape()
    stroke(255)
    noFill()
    angle=0
    while angle<TWO_PI*d:
        r = cos(k * angle) * 200
        x = r * cos(angle)
        y = r * sin(angle)
        vertex(x,y)
        angle+=0.02
    endShape(CLOSE)
    if keyPressed:
        if key=='z':
            d = d + 1 if d < 10 else 1 
        elif key=='x':
            d = d - 1 if d > 1 else 10
    

    
