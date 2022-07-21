#task : accept 5 student name and store in list.
student_list=[]
for i in range(1,6):
    name = input("enter student name:")
    student_list.append(name)
    print(student_list)