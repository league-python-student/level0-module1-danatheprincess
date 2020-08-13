from tkinter import messagebox, simpledialog, Tk
window=Tk()
window.withdraw()
secret= "birthday"
message=simpledialog.askstring("","Enter SECRET MESSAGE")
messagebox.showinfo("","if you want to see the secret message you should guess the password first")
password=simpledialog.askstring("","Enter password")
if password==secret:
    messagebox.showinfo("",message)
else:
    messagebox.showinfo("","INTRUDER")