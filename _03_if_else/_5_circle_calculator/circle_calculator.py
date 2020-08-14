# Write a Python program that asks the user for the radius of a circle.
from tkinter import messagebox, simpledialog, Tk
window=Tk()
window.withdraw()
import math

# Next, ask the user if they would like to calculate the area or circumference of a circle.
like=simpledialog.askstring("","Would you like to calculate the area or circumference of a circle")
radius=simpledialog.askinteger("","Enter a radius")
# If they choose area, display the area of the circle using the radius.
if  like == "area":
    area = math.pi * radius * radius
    messagebox.showinfo("",area)
else:
    cir=math.pi*radius*2
    messagebox.showinfo("",cir)
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 