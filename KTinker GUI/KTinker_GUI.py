from tkinter import *
from math import sqrt
a=b=c=0
a=2
b=5
c=-3
#0.5 and -3
print(f"{a}x**2+({b}x)+({c})")
D=b**2-4*a*c
if D>0:
    print("There are 2 roots")
    x1=(-1*b+sqrt(D))/(2*a)
    x2=(-1*b-sqrt(D))/(2*a)
    print()
    print(f"x1={x1}")
    print(f"x2={x2}")
elif D==0:
    print("Roots are the same")
    x=(-1*b)/(2*a)
    print(f"x={x}")
else:
    print("There are no roots. D<0")
