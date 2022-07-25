from tkinter import*
root=Tk()
root.title("new window")

def open():
    top=Toplevel()
    top.title("my second window")
    lbl=Label(top , text="hello world!").pack()



btn=Button(root , text="open second window" , command=open)
btn.pack()


root.mainloop()
