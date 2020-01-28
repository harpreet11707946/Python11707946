#program to calculate distance between two variables
import math
x1=int(input("enter number x1"))
x2=int(input("enter number x2"))
y1=int(input("enter number y1"))
y2=int(input("enter number y2"))
x=int(x2-x1)
print(x)
y=int(y2-y1)
print(y)
a=math.pow(x,2)
print(a)
b=math.pow(y,2)
print(b)
c=a+b
print(math.sqrt(c))
