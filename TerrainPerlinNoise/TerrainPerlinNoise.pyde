
scl=20 # scale of the "squares"
w, h = 1200, 1000
cols= w / scl
rows= h / scl
terrain= [[None for j in range(rows)] for i in range(cols)]
flying=0

def setup():
    global cols, rows, terrain
    size(600, 600, P3D)
    cols = w / scl
    rows = h / scl
    
    


def draw():
    global flying
    flying-=0.1
    yoff=flying
    for y in range(rows):
        xoff=0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -120, 120)
            xoff+=0.17
        yoff+=0.17
        
    background('#98d6ea')
    stroke(255, 100)
    fill('#235952')
    
    translate(width/2, height/2+50)
    rotateX(PI/3)
    translate(-w/2, -h/2)
    
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y]) #, random(-10, 10))
            vertex(x*scl, (y+1)*scl, terrain[x][y+1]) #, random(-10, 10))
        endShape()

            
#rect(x*scl, y*scl, scl, scl)
#terrain=[[map(noise(j, i), 0, 1, -50, 50) for j in range(rows)] for i in range(cols)]

            
