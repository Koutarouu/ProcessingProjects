from __future__ import division

def setup():
    size(800, 600)
    background(0)
    DDA(5, 4, 12, 7)
    bresenham(1, 1, 8, 5)

def DDA(x1, y1 ,x2 ,y2):
    dx = x2-x1
    dy = y2-y1
    steps = max(abs(dx), abs(dy))
    Xinc = dx/steps
    Yinc = dy/steps
    translate(width/2, height/2)
    scale(10)
    stroke(255)
    for i in range(steps):
        point(x1,y1)
        x1+=Xinc
        y1+=Yinc

def bresenham(x1,y1,x2,y2):
    x, y = x1, y1
    dx, dy = x2-x1, y2-y1
    p= 2*dy - dx
    stroke(255)
    translate(width/2, height/2)
    scale(10)
    while x<=x2:
        point(x, y)
        x+=1
        if p<0:
            p= p + 2*dy
        else:
            p= p + 2*dy - 2*dx
            y+=1
#x1,x2,y1,y2 = map(int, input().split())
#m = dy/dx
#DDA(5,5,12,5)
#DDA(5,7, 5, 12)
#DDA(5,7,10,15)
#DDA(12,9,17,14)
    
    
