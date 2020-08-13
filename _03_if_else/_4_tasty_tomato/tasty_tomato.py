from tkinter import simpledialog, messagebox, Tk, Canvas

windowWidth = 600
windowHeight = 600

root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="#DDDDDD")
canvas.grid()

#1. Ask the user what color tomato they would like and save their response   
#   You can give them up to three choices 
tasty=simpledialog.askstring("","what color would you like your tomato,powder blue,thistle,or tomato")

#2. use if-else statements to draw the tomato in the color that they chose
fill = "red"
if tasty=="powder blue":
    fill = "powderblue"
elif tasty=="thistle":
    fill="thistle"
elif tasty=="tomato":
    fill="tomato"
#   you can modify the code below or draw your own tomato
canvas.create_oval(75, 200, 400, 450, fill=fill, outline="")
canvas.create_oval(200, 200, 525, 450, fill=fill, outline="")


canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
    




root.mainloop()
