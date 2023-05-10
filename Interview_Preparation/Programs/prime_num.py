num = int(input("enter num: "))
if all(num % i !=0 for i in range(2, num)):
    print(num,"prime num")
else:
    print(num," not prime num ")