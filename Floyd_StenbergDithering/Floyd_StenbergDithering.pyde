from __future__ import division


def setup():
    global kongroo
    size(1280, 640)
    kongroo = loadImage("kyouma.jpg")
    kongroo.filter(GRAY)
    image(kongroo, 0, 0)


def draw():
    def index(x, y, df):
        indx = x + y * kongroo.width
        c = kongroo.pixels[indx%len(kongroo.pixels)]
        r, g, b = red(c), green(c), blue(c)
        r = r + errR * df
        g = g + errG * df
        b = b + errB * df
        kongroo.pixels[indx%len(kongroo.pixels)] = color(r, g, b)

    kongroo.loadPixels()
    for y in range(kongroo.height):
        for x in range(kongroo.width):
            idx = x + y * kongroo.width
            pix = kongroo.pixels[idx%len(kongroo.pixels)]
            oldR, oldG, oldB = red(pix), green(pix) , blue(pix)
            factor = 5 # 4 factor means number of colors is 5 * 5 * 5
            newR = round(factor*oldR / 255) * (255/factor)
            newG = round(factor*oldG / 255) * (255/factor)
            newB = round(factor*oldB / 255) * (255/factor)
            kongroo.pixels[idx%len(kongroo.pixels)] = color(newR, newG, newB)

            errR = oldR - newR
            errG = oldG - newG
            errB = oldB - newB
            
            index(x+1, y, 7/16)
            index(x-1, y+1, 3/16)
            index(x  , y+1, 5/16)
            index(x+1, y+1, 1/16)

 
    kongroo.updatePixels()
    image(kongroo, 640, 0)
    noLoop()

    """
    pixel[x + 1][y    ] := pixel[x + 1][y    ] + quant_error × 7 / 16
    pixel[x - 1][y + 1] := pixel[x - 1][y + 1] + quant_error × 3 / 16
    pixel[x    ][y + 1] := pixel[x    ][y + 1] + quant_error × 5 / 16
    pixel[x + 1][y + 1] := pixel[x + 1][y + 1] + quant_error × 1 / 16
    """
