from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("messagebox")


#showinfo , showwarning , showerror , askquetion , askokcancel , askyesno

def popup():
    response= messagebox.askyesno("this is my popup"," hello world")
    Label(root , text=response).pack()
    if response == 1:
        Label(root , text="you clicked yes").pack()
    else:
        Label(root , text="you clicked no").pack()

Button(root , text="popup" , command=popup).pack()

root.mainloop()
