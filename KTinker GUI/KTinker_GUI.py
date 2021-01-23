from tkinter import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from random import choice
import os
colours=["BlueViolet","Brown","CadetBlue","Crimson","ForestGreen","Gold","Sienna","Violet","Black","RoyalBlue"]
def roots(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    D=b**2-4*a*c
    with open("variables.txt","w") as file:
        file.write(f"D={b}**2-4*{a}*{c}\n")
    with open("variables.txt","a") as f:
        if D>0:
            x1=(-1*b+sqrt(D))/(2*a)
            x2=(-1*b-sqrt(D))/(2*a)
            f.write(f"D>0\n\nThere are 2 roots for this equation\n\nx1={x1}\nx2={x2}")
            x=[x1,x2]
        elif D==0:
            x1=(-1*b)/(2*a)
            f.write(f"D=0\n\nThere roots are equal for this equation\nx1=x2={x1}")
            x=[x1]
        else:
            f.write(f"D<0\n\nThere no roots for this equation")
            x=False
        return x
def solve(event):
    a=enta.get()
    b=entb.get()
    c=entc.get()
    answer=roots(a,b,c)
    if type(answer)==list:
        if btn1.winfo_ismapped()==0:
            btn1.grid(column=0,row=4)
    lines=""
    with open("variables.txt","r") as f:
        if lbl.winfo_ismapped()==False:
            lbl_grp.forget()
            lbl.grid(column=1,row=0,rowspan=4)
        for i in f.readlines():
            lines+=i.strip("{}()")
        lbl.configure(text=lines,justify=LEFT)
def graph(event):
    lbl.forget()
    a=int(enta.get())
    b=int(entb.get())
    c=int(entc.get())
    answer=roots(a,b,c)
    if len(answer)==2:
        x=np.arange(answer[0],answer[1]+0.01,0.01)
    elif len(answer)==1:
        x=answer[0]
    y=a*x**2+b*x+c
    plt.plot(x,y,color=f"{choice(colors)})",lw=3)
    plt.show()
    if os.path.exists("graph.png"):
        os.remove("graph.png")
    fig.savefig("graph.png")
    img=PhotoImage(file=("graph.png"))
    lbl.configure(image=img)

scr=Tk()
scr.title("Square Equation")
scr.geometry("800x600")
enta=Entry(scr,width=15,fg="Crimson",font="Ariel 14",bd=5)
entb=Entry(scr,width=15,fg="Crimson",font="Ariel 14",bd=5)
entc=Entry(scr,width=15,fg="Crimson",font="Ariel 14",bd=5)

btn=Button(scr,width=15,text="Solve",font="Ariel 14",bd=5)
btn1=Button(scr,width=15,text="Build Graph",font="Ariel 14",bd=5)

lbl=Label(scr,width=34,height=7,bg="gray",fg="Crimson",bd=5,anchor=NW,text="The solution will be posted here",font="Ariel 14",justify=CENTER)
lbl_grp=Label(scr)

btn1.bind("<Button-1>",graph)
btn.bind("<Button-1>",solve)

enta.grid(column=0,row=0)
entb.grid(column=0,row=1)
entc.grid(column=0,row=2)
btn.grid(column=0,row=3)
lbl.grid(column=1,row=0,rowspan=4)

scr.mainloop()

#import os
#os.remove(filename)
#fig.savefig("graph.png")
#scr.iconbitmap()