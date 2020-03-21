def setup():
    size(720, 540)
    loadPixels()
    maxiter=500
    for y in range(height):
        for x in range(width):
            a = aa = map(x, 0, width , -1.8, 1.5)
            b = bb = map(y, 0, height, -1.8, 1.5)
            n = 0
            #z = 0
            while n < maxiter:
                real = a*a - b*b
                imaginary = 2 * a * b
                
                a = real + aa
                b = imaginary + bb
                if abs(real+imaginary) > 16: # not remain bounded
                    break
                n+=1
            bright = n*16 % 256
            #bright = map(sqrt(bright), 0, 1, 0, 255)
            if n == maxiter:
                bright = 0
    
            pix = x + y * width
            pixels[pix] = color(bright, bright, bright, 255)
    updatePixels()
    
