"""i = int(input("Enter a num: "))
rev = 0
x = i
while(i>0):
    rev = (rev*10)+i%10
    i = i//10
if(x==rev):
    print("palindrome number")
else:
    print("not palindrome")"""

#palindrome using string: ---> it will reverse the name 
a = input("Enter name: ")
b = a[-1::-1]
if(a==b):
    print("palindrome")
else:
    print("not palindrome")