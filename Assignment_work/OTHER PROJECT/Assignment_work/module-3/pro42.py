#Write a Python function to check whether a number is in a given range
range1 = range(2, 20 , 3)
num = int(input("enter a number:"))

if num in range1:
    print(num,'is present in the range.')
else:
    print(num,'is not present in the range.')