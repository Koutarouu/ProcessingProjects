scl=20
cols,rows = 0,0
zoff=0
particles=[0 for i in range(500)]
flowField = []

class Particle(object):
    def __init__(self, x, y):
        self.pos=PVector(x,y)
        self.vel=PVector(0,0) #PVector(0,0).random2D()
        self.acc=PVector(0,0)
        self.maxSpeed = 2
        self.prevPos = self.pos.copy()
        self.h = 0
    
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.maxSpeed)
        self.pos.add(self.vel)
        self.acc.mult(0)
    
    def follow(self, vectors):
        x = floor(self.pos.x / scl)
        y = floor(self.pos.y / scl)
        idx = x + y * (width / scl)
        force = vectors[idx%len(vectors)]
        self.applyForce(force)
    
    def applyForce(self, force):
        self.acc.add(force)
    
    def show(self):
        stroke(self.h, 255, 255, 5)
        self.h = (self.h+1) % 256
        line(self.pos.x, self.pos.y, self.prevPos.x, self.prevPos.y)
        self.updatePrev()
        #point(self.pos.x, self.pos.y)
    
    def updatePrev(self):
        self.prevPos.x = self.pos.x
        self.prevPos.y = self.pos.y
        
    def edges(self):
        if self.pos.x > width:
            self.pos.x = 0
            self.updatePrev()
        if self.pos.x < 0:
            self.pos.x = width
            self.updatePrev()
        if self.pos.y > height:
            self.pos.y = 0
            self.updatePrev()
        if self.pos.y < 0:
            self.pos.y = height
            self.updatePrev()
    
def setup():
    global cols, rows, particles, flowField
    size(400, 400)
    colorMode(HSB, 255)
    background(51)
    cols = width/scl
    rows = height/scl
    flowField= [0]*(cols*rows)
    for i in range(500):
        particles[i] = Particle(random(width), random(height))

def draw():
    global zoff, particles, flowField
    yoff=0
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            idx = x + y * cols
            angle = noise(xoff, yoff, zoff) * TWO_PI * 4
            v = PVector().fromAngle(angle) # (random(TWO_PI))
            v.setMag(1)
            flowField[idx] = v
            xoff+=0.1
        yoff+=0.1
        
        zoff+=0.0003
    for i in range(len(particles)):
        particles[i].follow(flowField)
        particles[i].update()
        particles[i].edges()
        particles[i].show()




"""
push()
translate(x*scl, y*scl)
rotate(v.heading()) #calculate the angle of rotation of the vector
strokeWeight(1)
line(0, 0, scl, 0)
pop()
"""
#frameRate(4)
#randomSeed(10)
#fill(r)
#rect(x * scl, y * scl, scl, scl)
#frameRate(4)
