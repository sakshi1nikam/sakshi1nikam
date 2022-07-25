from tkinter import*

root=Tk()
root.title("simple calculator")

e=Entry(root , width=35 , borderwidth=5)
e.grid(row=0 , column=0 , columnspan=3 ,padx=10 , pady=10)
#define functins 

def btn_click(num):
    current=e.get()
    e.delete(0 ,END )
    e.insert(0 ,str(current) + str(num))

def btn_clear():
    e.delete(0 ,END)

def btn_add():
    num=e.get()
    global f_num
    global math
    math= "addition"
    f_num= int(num)
    e.delete(0 , END)

def btn_equal():
    num1=e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0 , f_num+ int(num1))
    if math == "subtraction":
        e.insert(0 , f_num- int(num1))
    if math == "multiplication":
        e.insert(0 , f_num * int(num1))
    if math == "division":
        e.insert(0 , f_num/ int(num1))

def btn_sub():
    num=e.get()
    global f_num
    global math
    math= "subtraction"
    f_num= int(num)
    e.delete(0 , END)
def btn_mul():
    num=e.get()
    global f_num
    global math
    math= "multiplication"
    f_num= int(num)
    e.delete(0 , END)
def btn_div():
    num=e.get()
    global f_num
    global math
    math= "division"
    f_num= int(num)
    e.delete(0 , END)

#define buttons
button_1=Button(root, text="1" , padx=42 , pady=20, command=lambda:btn_click(1))
button_2=Button(root, text="2" , padx=42 , pady=20, command=lambda:btn_click(2))
button_3=Button(root, text="3" , padx=42 , pady=20, command=lambda:btn_click(3))
button_4=Button(root, text="4" , padx=42 , pady=20, command=lambda:btn_click(4))
button_5=Button(root, text="5" , padx=42 , pady=20, command=lambda:btn_click(5))
button_6=Button(root, text="6" , padx=42 , pady=20, command=lambda:btn_click(6))
button_7=Button(root, text="7" , padx=42 , pady=20, command=lambda:btn_click(7))
button_8=Button(root, text="8" , padx=42 , pady=20, command=lambda:btn_click(8))
button_9=Button(root, text="9" , padx=42 , pady=20, command=lambda:btn_click(9))
button_0=Button(root, text="0" , padx=42 , pady=20, command=lambda:btn_click(0))
button_add=Button(root , text="+" , padx=42 ,pady=20 , command=btn_add)
button_equal=Button(root , text="=" ,padx=91 ,pady=20, command=btn_equal )
button_clear=Button(root , text="c" ,padx=91,pady=20 , command=btn_clear)
button_sub=Button(root , text="-" , padx=42 ,pady=20 , command=btn_sub)
button_mul=Button(root , text="*" , padx=42 ,pady=20 , command=btn_mul)
button_div=Button(root , text="/" , padx=42 ,pady=20 , command=btn_div)


# put buttons on the screen 

button_1.grid(row= 3, column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)
button_0.grid(row= 4, column=0)

button_add.grid(row=5 , column=0)
button_equal.grid(row=5, column=1 , columnspan=2)
button_clear.grid(row=4 ,column=1,columnspan=2)

button_sub.grid(row=6 , column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()
