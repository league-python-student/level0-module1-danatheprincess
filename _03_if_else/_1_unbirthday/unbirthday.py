from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
unbirthday=simpledialog.askstring("","when in your  birthday?")
if unbirthday=="August 13":
    messagebox.showinfo("It's your Birthday","HAPPY BIRTHDAY")
else:
    messagebox.showinfo("","Have a very merry UNbirthday ")