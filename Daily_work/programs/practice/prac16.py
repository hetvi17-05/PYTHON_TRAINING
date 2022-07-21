#accept 5 numbers and fing even and odd number
from asyncio import events


for i in range(1,6):
    num=int(input("enter a number:"))
    if num%2==0:
        print("even")
    else:
        print("odd")