from tkinter import *
from math import sqrt
def roots(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    D=b**2-4*a*c
    with open("variables.txt","w") as file:
        file.write(f"D={b}**2-4*{a}*{c}\n\n")
    with open("variables.txt","a") as f:
        if D>0:
            x1=(-1*b+sqrt(D))/(2*a)
            x2=(-1*b-sqrt(D))/(2*a)
            f.write(f"D>0\n\nThere are 2 roots for this equation\n\nx1={x1}\nx2={x2}")
        elif D==0:
            x=(-1*b)/(2*a)
            f.write(f"D=0\n\nThere roots are equal for this equation\nx1=x2={x}")
        else:
            f.write(f"D<0\n\nThere no roots for this equation")
def confirm(event):
    a=enta.get()
    b=entb.get()
    c=entc.get()
    roots(a,b,c)
    lines=""
    with open("variables.txt","r") as f:
        for i in f.readlines():
            lines+=i.strip("{}()")
        lbl.configure(text=lines,justify=LEFT)
    #btn1=Button(scr,width=15,text="Graph",font="Ariel 14",bd=10)
scr=Tk()
scr.title("Square Equation")
scr.geometry("600x400")
enta=Entry(scr,width=15,fg="Crimson",font="Ariel 14",bd=10)
entb=Entry(scr,width=15,fg="Crimson",font="Ariel 14",bd=10)
entc=Entry(scr,width=15,fg="Crimson",font="Ariel 14",bd=10)
btn=Button(scr,width=15,text="Confirm",font="Ariel 14",bd=10)
lbl=Label(scr,width=34,height=7,bg="gray",fg="Crimson",bd=10,anchor=NW,text="The solution will be posted here",font="Ariel 14",justify=CENTER)

btn.bind("<Button-1>",confirm)
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