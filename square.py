class Square:
    def __init__(self,x,y,side,color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x
    def draw(self,canvas):
        canvas.canvas[self.y:self.side + self.y, self.x:self.x + self.side] = self.color
