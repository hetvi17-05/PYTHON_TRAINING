#accept 5 no.s and count no.of even and no.of odd numbers

even_count=0
odd_count=0
for i in range(1,6):
    num = int(input("enter a number:"))
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
    print("even count=",even_count)
    print("odd count=",odd_count)
     
