import numpy as np
from PIL import Image
class Canvas:
    def __init__(self,width,height,color):
        self.color = color
        self.height = height
        self.width = width
        self.canvas=np.zeros((self.width,self.height,3),dtype=np.uint8())
        self.canvas[:]=self.color
    def make(self,img_path):
        img=Image.fromarray(self.canvas,mode="RGB")
        img.save(img_path)

