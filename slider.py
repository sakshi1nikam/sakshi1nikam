from tkinter import*

root=Tk()
root.title("slider")
root.geometry("400x400")


vertical=Scale(root , from_=0 , to_=200)
vertical.pack()

horizontal=Scale(root , from_=0 , to_=200 , orient=HORIZONTAL)
horizontal.pack()

my_label= Label(root, text=horizontal.get())
my_label.pack()


def slide():
    my_label= Label(root, text=horizontal.get())
    my_label.pack()
    
my_btn=Button(root , text="click me" , command=slide).pack()

root.mainloop()
