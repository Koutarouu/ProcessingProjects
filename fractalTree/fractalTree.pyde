angle = 0

def mouseWheel(event): 
    global angle
    if event.count<1:
        angle= angle + 0.1 if angle<(2*PI) else 2*PI
    else:
        angle= angle - 0.1 if angle>0 else 2*PI

def setup():
    size(500, 500)

def draw():
    background(183, 233, 255)    
    strokeWeight(4)
    stroke(216, 201, 204)
    translate(width/2, height) # moving the origin to the bottom middle
    branch(150)

def branch(leng):
    global angle
    line(0, 0, 0, -leng)
    translate(0, -leng) # translate up to the top

    if leng>4:
        if 4<=leng<=5:
            strokeWeight(2)
            stroke(255, 183, 197)
        push()
        rotate(angle)
        branch(leng*0.67)
        pop()
        push()
        rotate(-angle)
        branch(leng*0.67)
        pop()
    #line(0, 0, 0, -leng*0.67)
