n = int(input("enter num:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

#pattern a triangle using function
def triangle(n):
    k = n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k-1
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
n = 5
triangle(n)

#using for loop with c++
"""
for i in range(1,6):
    print(" "*(9-i)," *"*i) """


n = int(input("Enter a num: "))
for num in range(n):
    for j in range(n-num-1):
        print(" ",end="")
    for j in range(1*num+1):
        print(num,end="")
    print()