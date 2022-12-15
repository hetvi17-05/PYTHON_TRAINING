
# take 5 numbers from user

for i in range(1,6):
    num1 =  int(input("enter a nunber"+str(i)+" : "))

#format function:

num1 = 10
num2 = 20

print(f"{num1} + {num2} = {num1 + num2}")

for i in range(1,6):
        num1 = int(input(f"enter number {i} : "))

#even-odd
for i in range(1,6):
    
    num = int(input("enter a number:"))
    if num%2==0:
        print("even number:")
    else:
        print("odd number:")

#accept 5 marks from user and check pass or fail

for i in range (1,6):

    marks= int(input("enter a marks:"))
    if marks<=35:
        print("pass")
    else:
        print("fail")

#accept 5 num positive and negative
for i in range(1,6):
    num1= int(input("enter a num:"))
    if num1<=0:
        print("negative")
    else:
        print("positive")

#take 5 num and count total neg num and pos num
    positive_num=0
    negative_num=0
    for i in range(1,6):
        num = int(input("enter a number:"))
        if num>0:
            positive_num+=1
        else:
            negative_num+=1
        print("positive num=",positive_num)
        print("negative num=",negative_num)

#take 5 num and count total even num and odd num
    even_num=0
    odd_num=0
    for i in range(1,6):
        num = int(input("enter a number:"))
        if num%2==0:
            even_num+=1
        else:
            odd_num+=1
        print("even num=",even_num)
        print("odd num=",odd_num)

#take 5 marks from user and count passing subject and failing subjectcs

    p_count=0
    f_count=0
    for i in range(1,6):
        num = int(input("enter a number:"))
        if num1<35:
            p_count+=1
        else:
            f_count+=1
        print("p count=",p_count)
        print("f count=",f_count)

# accept 5 subject and count total marks

sum = 0
for i in range(1,6):
    marks = int(input("enter number"))
    sum+=marks
print(sum)