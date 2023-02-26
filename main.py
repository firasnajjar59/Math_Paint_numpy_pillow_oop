from canvas import Canvas
from rectangle import Rectangle
from square import Square
canvas_width=int(input("Enter the canvas width. "))
canvas_height=int(input("Enter the canvas height. "))
canvas_color=input("Enter the canvas background color.(black,white) ").lower()
canvas_bg={"white":(255,255,255),"black":(0,0,0)}
canvas=Canvas(width=canvas_width,height=canvas_height,color=canvas_bg[canvas_color])

while True:
    shape=input("Enter shape to draw,(Rectangle,Square). To finish enter 'Q'").lower()
    if shape=="rectangle":
        r_x=int(input("Enter X position. "))
        r_y=int(input("Enter Y position. "))
        r_width=int(input("Enter width. "))
        r_height=int(input("Enter height. "))
        r_r=int(input("Enter the red color.(between 0-255) "))
        r_g=int(input("Enter the green color.(between 0-255) "))
        r_b=int(input("Enter the blue color.(between 0-255) "))
        rec=Rectangle(x=r_x,y=r_y,width=r_width,height=r_height,color=(r_r,r_g,r_b))
        rec.draw(canvas)

    elif shape=="square":
        s_x=int(input("Enter X posion. "))
        s_y=int(input("Enter Y posion. "))
        s_side=int(input("Enter side length. "))
        s_r=int(input("Enter the red color.(between 0-255) "))
        s_g=int(input("Enter the green color.(between 0-255) "))
        s_b = int(input("Enter the blue color.(between 0-255) "))
        square=Square(x=s_x,y=s_y,side=s_side,color=(s_r,s_g,s_b))
        square.draw(canvas)
    elif shape=="q":
        break
file_name=input("Give the file a name ").lower()
canvas.make(file_name)