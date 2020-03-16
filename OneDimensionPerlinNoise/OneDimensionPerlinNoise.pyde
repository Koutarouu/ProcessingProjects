inc=0.01
start=0

def setup():
    size(400,400)
    
    
def draw():
    global start
    background(51)
    stroke(255)
    #noFill()
    beginShape()
    xoff=start
    for x in range(width):
        n = map(noise(xoff), 0, 1, -50, 50)
        s = map(cos(xoff), -1, 1, 0, height)
        y = s + n
        # y = height/2 + sin(xoff) * height/2
        vertex(x, y)
        xoff+=inc
    endShape()
    start+=inc
    # noLoop()
    


"""
#y=random(height)
#y=noise(xoff)*height


xoff1=0
xoff2=10000
global xoff1, xoff2
x=noise(xoff1)*width
y=noise(xoff2)*height
ellipse(x, y, 20, 20)
xoff1+=0.05
xoff2+=0.05
"""
