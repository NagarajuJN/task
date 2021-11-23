from tkinter import *

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val = " "
    data.set(" ")

def btnEquals():
    global  val
    result=str(eval(val))
    data.set(result)

root=Tk()
root.title("Calculator")
root.geometry("371x475+500+200")
val=" "
data=StringVar()
display=Entry(root,textvariable=data,bd=35,bg="powder blue",font=("ariel",20,"bold"),justify="right")
display.grid(row=0,columnspan=4)
btn7=Button(root,text=7,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text=8,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text=9,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)
btn_div=Button(root,text="/ ",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('/'))
btn_div.grid(row=1,column=3)
btn4=Button(root,text=4,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text=5,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text=6,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)
btn_mul=Button(root,text="*",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btn_mul.grid(row=2,column=3)
btn1=Button(root,text=1,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text=2,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text=3,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
btn_sub=Button(root,text=" - ",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('-'))
btn_sub.grid(row=3,column=3)
btn =Button(root, text=".", font=("ariel", 12, "bold"), bd=12, height=2, width=6,command=lambda:btnClick('.'))
btn.grid(row=4,column=0)
btn0=Button(root,text=0,font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0))
btn0.grid(row=4,column=1)
btn=Button(root,text="=",bg="yellow",font=("ariel",14,),bd=12,height=2,width=6,command=btnEquals)
btn.grid(row=4,column=2)
btn_add=Button(root,text=" + ",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('+'))
btn_add.grid(row=4,column=3)
btnc=Button(root,text=" Clr ",bg="red",font=("ariel",14,"bold"),bd=12,height=2,width=6,command=btnClear)

btnc.grid(row=5,columnspan="5",)
mainloop = root.mainloop()