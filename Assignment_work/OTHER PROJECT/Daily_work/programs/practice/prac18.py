#accept 5 no.s from user and count no of positive number and negative number.
positive_number=0
negative_number=0
for i in range(1,6):
    num = int(input("enter a number:"))
    if num>=0:
        positive_number+=1
    else:
        negative_number+=1
    print("positive number=",positive_number)
    print("negative number=",negative_number)
     
