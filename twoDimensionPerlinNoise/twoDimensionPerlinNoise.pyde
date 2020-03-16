
def setup():
    size(400,400)
    #pixelDensity(1)
    
def draw():
    yoff=0
    loadPixels()
    noiseDetail(14, 0.6)
    for y in range(height):
        xoff = 0
        for x in range(width):
            r=noise(xoff, yoff) * 255
            pixels[x+y*width] = color(r,r,r,255)
            xoff+=0.005
        yoff+=0.005
    updatePixels()
    noLoop()
