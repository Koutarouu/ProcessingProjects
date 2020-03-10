#variables: F+-[]
#axiom: F
#rules: F -> FF+[+F-F-F]-[-F+F+F]
#EXAMPLE
#rules = {'A': 'AB', 'B': 'A'}
#axiom='A'
#F- Go forward + turn right - turn left [ Save the position ] Restore the last position
axiom='F'
rules = {'F': 'FF+[+F-F-F]-[-F+F+F]'}
leng=200
depth=1

def setup():
    size(800, 540)
    turtle()
    
def turtle():
    global axiom, leng, depth
    resetMatrix()
    # background(234, 212, 204)
    background(loadImage("tree.jpg"))
    translate(width/2, height)
    
    for i in axiom:
        if i=='F':
            if depth<=3:
                strokeWeight(2)
                stroke(185, 134, 126)
            elif depth<=5:
                strokeWeight(1)
                stroke(236, 171, 204)
            line(0, 0, 0, -leng)
            translate(0, -leng)
        elif i=='+':
            rotate(PI/6)
        elif i=='-':
            rotate(-PI/6)
        elif i=='[':
            push()
            depth= depth + 1 if depth<5 else 4
        elif i==']':
            pop()
            depth= depth - 1 if depth>0 else 1
    leng/=2
    depth+=1
    
def LsystemTest():
    global axiom
    sentence = axiom
    new_sentence=[]
    for i in sentence:
        if i in rules:
            new_sentence.append(rules[i])
        else:
            new_sentence.append(i)
    axiom = "".join(new_sentence)
    print(sentence)

def mouseClicked():
    LsystemTest()
    turtle()
    
def draw():
    return 0
