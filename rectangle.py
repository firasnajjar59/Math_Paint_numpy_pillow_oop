import numpy as np
from PIL import Image
class Rectangle:
    def __init__(self,x,y,width,height,color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        print(self.color)
    def draw(self,canvas):
        canvas.canvas[self.y:self.height+self.y,self.x:self.x+self.width]=self.color