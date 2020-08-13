from tkinter import messagebox, simpledialog, Tk
window=Tk()
window.withdraw()
remarkable=simpledialog.askstring("","Enter a name Daniel,David,or Sarika")
if remarkable=="Daniel":
    messagebox.showinfo("","He is really smart")
elif remarkable=="David":
    messagebox.showinfo("","He is funny")
elif remarkable=="Sarika":
    messagebox.showinfo("","She is nice and good at coding")

else:
    messagebox.showinfo("","I Don't know you ")

