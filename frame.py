from tkinter import*
root=Tk()
root.title("frames")

frame=LabelFrame(root  , padx=50 , pady=50)
frame.pack(padx=10 , pady=10)

b=Button(frame , text="dont click here" )

b.grid(row=1 ,column=0)


b1=Button(frame , text ="click here" )

b1.grid(row=1 , column=1)
root.mainloop()
