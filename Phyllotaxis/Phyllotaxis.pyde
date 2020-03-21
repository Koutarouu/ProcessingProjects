n = 0
c = 8

def setup():
    size(400, 400)
    background(0)
    colorMode(HSB) # Hue Saturation Brightness
    
def draw():
    global n, c
    if n<500:
        a = n * radians(137.6)
        r = c * sqrt(n)
        
        x = r * cos(a) + width / 2
        y = r * sin(a) + height / 2
        
        fill((a - r)%256 , 255,  200)
        ellipse(x, y, 8, 8)
        
        n+=1
    
