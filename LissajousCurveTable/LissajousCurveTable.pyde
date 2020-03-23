from Curves import Curve

ss = False
angle = 0
w = h = 200
cols = rows = 0
curves=[]
def setup():
    global cols, rows, curves
    fullScreen()
    cols = width / w - 1
    rows = height / h - 1
    curves = [[Curve() for j in range(cols)] for i in range(rows)]
    #pixelDensity(displayDensity())


def draw():
    global angle, curves, ss
    background('#2f2f48')

    d = w - w * 0.2
    r = d / 2
    noFill()
    for j in range(cols):
        cx = w + j * w + w / 2
        cy = w / 2
        stroke('#0881d1')
        strokeWeight(1)
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (j+1) - HALF_PI)
        y = r * sin(angle * (j+1) - HALF_PI)
        stroke(255)
        strokeWeight(8)
        point(cx + x, cy + y)
        stroke(86, 150)
        strokeWeight(2)
        line(cx + x, 0, cx + x, height)
        for i in range(rows):
            curves[i][j].setX(cx + x)

    for i in range(rows):
        cx = h / 2
        cy = h + i * h + h / 2
        stroke('#ba0b32')
        strokeWeight(1)
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (i+1) - HALF_PI)
        y = r * sin(angle * (i+1) - HALF_PI)
        stroke(255)
        strokeWeight(8)
        point(cx + x, cy + y) # here is the magic
        stroke(86, 150)
        strokeWeight(2)
        line(0, cy + y, width, cy + y)
            
        for j in range(cols):
            curves[i][j].setY(cy + y)
    
    for i in range(rows):
        for j in range(cols):
            curves[i][j].add_point()
            curves[i][j].show()
    angle-=0.05
    
    if angle < -TWO_PI:
        for i in range(rows):
            for j in range(cols):
                curves[i][j].reset()
        if not ss:
            saveFrame("table####.png")
            ss=True
        angle = 0
          
