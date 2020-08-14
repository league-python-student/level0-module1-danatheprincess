import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    liz=turtle.Turtle()
    liz.setheading(0)
    liz.width(10)
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring("","what shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape=="square":
        liz.color('thistle')
        for i in range(4):
            liz.forward(100)
            liz.right(90)
    elif shape=="tringle":
        liz.color("powderblue")
        for i in range(3):
            liz.forward(200)
            liz.left(120)
    elif shape=="pentagon":
        liz.color('pink')
        for i in range(5):
            liz.forward(100)
            liz.left (360/5)
    elif shape=="rectangle":
        liz.color('lightgreen')
        for i in range(2):
            liz.forward(100)
            liz.right(90)
            liz.forward(60)
            liz.right(90)
    elif shape=="rhombus":
        liz.color('cornflowerblue')
        for i in range(4):
            liz.forward(100)
            liz.left(120)
            liz.forward(100)
            liz.right(120)
    # Call the turtle .done() method
    turtle.done()
    window.mainloop()