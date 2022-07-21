status = True
while status:
    marks = int(input("enter your marks:"))
    if marks<=35:
        print("fail")
        status = False
    else:
        print("pass")