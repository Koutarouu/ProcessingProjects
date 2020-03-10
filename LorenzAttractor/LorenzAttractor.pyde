add_library('peasycam')
x,y,z=0.01,0.01,0.01
sigma=10
rho=28
betha=2.666667
points=[] # in order to manipulate the system [x, y, z]

def setup():
    size(800, 600, P3D)
    colorMode(HSB) #High saturation 
    cam = PeasyCam(this, 500)

    
def draw(): # this applies the changue along the time frame by frame
    global x, y, z
    background(51)
    dt = 0.01 # changue in time
    dx = (sigma * (y - x)) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - betha * z) * dt
    x = x + dx # x plus that changue in x
    y = y + dy
    z = z + dz
    
    points.append([x, y, z])
    
    translate(0, 0, -80)
    scale(5)
    stroke(255, 100)
    noFill() # para no rellenar con vertex
    
    hu=0
    beginShape()
    for i in range(len(points)):
        stroke(hu, (2*hu)%255, (3*hu)%255)
        vertex(points[i][0], points[i][1], points[i][2])# point
        offset = [random(-1.0, 1.0)*0.1, random(-1.0, 1.0)*0.1, random(-1.0, 1.0)*0.1]
        for j in range(len(points[i])):
            points[i][j] += offset[j]
        hu = (hu + 0.1)%255
    endShape()
    # print(x,y,z)
    
