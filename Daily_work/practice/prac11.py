#accept marks from student: and give him appropriate grades 
#eg : above 70: A, 60-70: B, 50-60: C, 40-50: D, Below 35: Fail.

marks= int(input("enter a marks:"))
if marks>=70:
    print("a grade")
elif marks>=60 and marks<=70:
    print("b grade")
elif marks>=50 and marks<=60:
    print("c grade")
elif marks>=40 and marks<=50:
    print("d grade")
else:
    print("fail")