class Curve:
    
    def __init__(self):
        self.path = []
        self.current = PVector()
        
    def setX(self, x):
        self.current.x = x
        
    def setY(self, y):
        self.current.y = y
    
    def add_point(self):
        self.path.append(self.current)
    
    def show(self):
        stroke('#2b7b66')
        strokeWeight(2)
        beginShape()
        for v in self.path:
            vertex(v.x, v.y)
        endShape()
        
        strokeWeight(8)
        point(self.current.x, self.current.y)
        self.current = PVector()
    
    def reset(self):
        self.path = []
