#write a python program to get the largest number, smallest num and sum of all from a list.
mylist=[]
num = int(input("enter a number:"))
for i in range(1,6):
    num = int(input("enter num:"))
    mylist.append(num)
    print("maximum  num in the list is:",max(mylist))
else:
    print("minimum  num in the list is:",min(mylist))
 