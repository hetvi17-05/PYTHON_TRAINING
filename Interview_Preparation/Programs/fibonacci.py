"""num = int(input("Enter Number: "))
First_val = 0
Second_val = 1
for n in range(0, num):
    if(n<=1):
        a = n
    else:
        a = First_val + Second_val
        First_val = Second_val
        Second_val = a
    print(a)"""

n = int(input("enter num: "))
x = 0
y = 1
z = 0
while(z<=n):
    print(z)
    x = y
    y = z
    z = x+y