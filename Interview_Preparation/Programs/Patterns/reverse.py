#by using sort we can find smallest num
"""l=[40,38,-1]
l.sort()
print("num:",l[0])"""

#count total number in digit
"""num = 4321
count = 0
while num != 0:
    num //= 10
    count+=1
print(count)"""


# by using array find samlest num 
l=(40,29,-1)
a = l[0]
for i in range(len(l)):
    if l[i] < a:
        a = l[i]
print(a)

# using inbuilt function reverse number
l= [1,2,3,4]
l.reverse()
print(l)

# without using inbuilt functoin reverse
l = 6541232
print(str(l)[::-1])

#find largest num
l=[10,20,50]
a = l[0]
for i in range(len(l)):
    if l[i] > a:
        a = l[i]
print(a)

#sort
l=[0,0,1,0,1,3,5,2,1,6]
l.sort()
print(l)

#swap two num
x = 4
y = 9
x,y = y,x
print("x :",x)
print("y :",y)

#find sum of integer
l = input("enter name:")
sum = 0
for i in l:
    if i.isdigit():
        sum = sum+int(i)
print(sum)
 #enter name:sad876543dcvbj987 ---> 57(it will plus all the num 8+7+6+5+4+3+9+8+7=57)