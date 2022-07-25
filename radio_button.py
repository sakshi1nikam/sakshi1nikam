from tkinter import*
root =Tk()
root.title("radio button")


#r =InVar()
#r.set("2")


MODES=[
    ("maths","maths"),
    ("science","science"),
    ("history","history"),
    ("geogrphy","geogrphy")
]
sub= StringVar()
sub.set("maths")

sub1= StringVar()
sub1.set("history")

for text , i in MODES:
    Radiobutton(root , text=text , variable=sub1 , value=i).pack(anchor=W)


def clicked(value):
    mylabel=Label(root , text=value)
    mylabel.pack()

#Radiobutton(root , text ="option 1" ,variable=r , value=1 , command=lambda:clicked(r.get())).pack()


#Radiobutton(root , text ="option 2" ,variable=r , value=2).pack()

mybutton=Button(root , text="click me" ,command=lambda:clicked(sub.get()))
mybutton.pack()

#mylabel=Label(root , text=sub.get())
#mylabel.pack()
root.mainloop()
