#factorial_number
#5=5*4*3*2*1(to accept the value from user)
num = int(input("enter a number: "))
if num>0:
    f = 1
    for i in range(1, num+1):
        f*=i
        print("factorial=",f)
else:
    print("invalid input")