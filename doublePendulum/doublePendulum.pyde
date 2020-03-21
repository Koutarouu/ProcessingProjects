from __future__ import division

l1 = l2 =200
m1 = m2 = 30
an1, an2 = PI/2, PI/4
a1_v = a2_v = 0
g = 1
px2 = py2 = -1
cx = cy = 0
canvas = None

def setup():
    global canvas, cx, cy
    size(900, 600)
    cx = width/2
    cy = 70
    canvas = createGraphics(width, height)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()

def draw():
    global an1, an2, canvas, a1_v, a2_v, px2, py2
    num1 = -g * (2*m1 + m2) * sin(an1)
    num2 = -m2 * g * sin(an1 - 2*an2)
    num3 = -2 * sin(an1 - an2) * m2
    num4 = a2_v * a2_v * l2 + a1_v * a1_v * cos(an1 - an2)
    den = l1 * (2*m1 + m2 - m2 * cos(2*an1 - 2*an2 ))
    
    a1_a = (num1 + num2 + num3*num4) / den
    
    num1 = 2 * sin(an1 -  an2) 
    num2 = (a1_v * a1_v * l1 * (m1 + m2))
    num3 = g * (m1 + m2) * cos(an1)
    num4 = a2_v * a2_v * l2 * m2 * cos(an1 - an2)
    den = l2 * (2*m1 + m2 - m2 * cos(2*an1 - 2*an2 ))

    a2_a = (num1*(num2 + num3 + num4)) / den
    
    image(canvas, 0, 0)
    stroke(51)
    strokeWeight(2)
    noFill()
    translate(cx, cy)
    
    x1 = l1 * sin(an1)
    y1 = l1 * cos(an1)
    
    x2 = x1 + l2 * sin(an2)
    y2 = y1 + l2 * cos(an2)
    
    line(0, 0, x1, y1)
    ellipse(x1, y1, m1, m1)
    
    line(x1, y1, x2, y2)
    ellipse(x2, y2, m2, m2)
    
    a1_v += a1_a
    a2_v += a2_a
    an1 += a1_v
    an2 += a2_v
    
    canvas.beginDraw()
    canvas.colorMode(HSB)
    canvas.translate(cx, cy)
    canvas.strokeWeight(1)
    canvas.stroke(180, (51.8* an2)%100, 250)#(48 * an1)%100, 100, 100)
    if frameCount > 1:
        canvas.line(px2, py2, x2, y2)
    canvas.endDraw()
    
    px2 = x2
    py2 = y2
    
