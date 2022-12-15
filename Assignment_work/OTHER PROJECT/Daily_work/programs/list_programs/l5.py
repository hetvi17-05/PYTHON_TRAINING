#check enterd data is exist in list or not.
subject_list=["c","c++","java","python"]
subject=input("enter a subject:")
if subject not in subject_list:
    print("subject is not available")
else:
    print("subject is available")