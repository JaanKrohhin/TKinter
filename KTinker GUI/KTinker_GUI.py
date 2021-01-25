from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from random import choice
import os
colours=["BlueViolet","Brown","CadetBlue","Crimson","ForestGreen","Gold","Sienna","Violet","Black","RoyalBlue"]
rng=choice(colours)
def roots(a,b,c):
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
    friend=True
    try:
        a=float(enta.get())
    except:
        TypeError
        messagebox.showinfo("Error","'a' is not a valid number")
        friend=False
    try:
        b=float(entb.get())
    except:
        TypeError
        messagebox.showinfo("Error","'b' is not a valid number")
        friend=False
    try:
        c=float(entc.get())
    except:
        TypeError
        messagebox.showinfo("Error","'c' is not a valid number")
        friend=False
    if friend==False:
        pass
    else:
        answer=roots(a,b,c)
        if type(answer)==list:
            if btn1.winfo_ismapped()==0:
                btn1.grid(column=0,columnspan=2,row=4)
        elif type(answer)!=list:
            if btn1.winfo_ismapped()==1:
                btn1.grid_forget()
        lines=""
        with open("variables.txt","r") as f:
            for i in f.readlines():
                lines+=i.strip("{}()")
            lbl.configure(text=lines,justify=LEFT)
def graph(event):
    a=float(enta.get())
    b=float(entb.get())
    c=float(entc.get())
    answer=roots(a,b,c)
    if len(answer)==2:
        answer.sort()
        x=np.arange(answer[0],answer[1]+0.01,0.01)
    elif len(answer)==1:
        x=np.array(answer[0])
    y=a*x**2+b*x+c
    plt.xticks(np.arange(-15,16,3))
    plt.yticks(np.arange(-15,16,3))
    plt.grid(axis="both",c="black",lw=2,alpha=0.5)
    plt.grid(True)
    plt.plot(x,y,color=f"{rng}",lw=3)
    plt.show()
scr=Tk()
scr.title("Square Equation")
scr.geometry("600x300")
enta=Entry(scr,width=15,fg="Orange",font="Ariel 14",bd=5)
entb=Entry(scr,width=15,fg="Orange",font="Ariel 14",bd=5)
entc=Entry(scr,width=15,fg="Orange",font="Ariel 14",bd=5)

btn=Button(scr,width=20,text="Solve",font="Ariel 14",bd=5)
btn1=Button(scr,width=20,text="Graph",font="Ariel 14",bd=5)

lbl=Label(scr,width=34,height=7,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="The solution will be posted here",font="Ariel 14",justify=CENTER)
lbla=Label(scr,width=5,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="a=",font="Ariel 14",justify=CENTER)
lblb=Label(scr,width=5,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="b=",font="Ariel 14",justify=CENTER)
lblc=Label(scr,width=5,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="c=",font="Ariel 14",justify=CENTER)
btn1.bind("<Button-1>",graph)
btn.bind("<Button-1>",solve)

enta.grid(column=1,row=0)
entb.grid(column=1,row=1)
entc.grid(column=1,row=2)
btn.grid(column=0,columnspan=2,row=3)
lbl.grid(column=2,row=0,rowspan=4)
lbla.grid(column=0,row=0)
lblb.grid(column=0,row=1)
lblc.grid(column=0,row=2)

scr.mainloop()