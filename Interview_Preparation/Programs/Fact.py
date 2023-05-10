"""n = int(input("enter num:"))
factorial = 1
if int(n)>1:
    for i in range(1,int(n)+1):
        factorial = factorial*i
    print(factorial,"factorial")"""

#2 method
"""f = 1
for i in range(1,5):
    f*=i
print(f,"f")"""

n = 5
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end="")
    print()












#https://www.edureka.co/blog/python-program-to-check-leap-year/