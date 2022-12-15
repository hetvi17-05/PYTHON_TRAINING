counsellor = {}
student = {}
faculty = {}

menu = """
                    STUDENT MANAGMENT SYSTEM
                    
                    Press 1 add student
                    Press 2 remove student
                    Press 3 for view  all student
                    Press 4 view specific student
"""
status = True
while status:
    print(menu)
    specification  = {}
    choice = int(input("enter your choice :"))
    if choice == 1:
        
        sr_no = int(input("enter your sr.no : "))
        first_name = input("enter your first name:")
        last_name = input("enter your last name:")
        contact_no = int(input("enter your contact no:"))
        subject = input("enter your subject:")
        subject_fees = int(input("enter fees:"))
    
        specification['sr_no'] = sr_no
        specification['first_name'] = first_name
        specification['last_name']= last_name
        specification['contact no'] = contact_no
        specification['subject'] = subject
        specification['fees'] = subject_fees

        counsellor[sr_no] = specification
        print(counsellor)
    elif choice==2:
        for k in counsellor.keys():
                print("------------------------------------------")
                print(f"student sr_no : {k} ")
                print(f"student first name : ",counsellor[k]["first_name"])
                print(f"student last name : {k} ",counsellor[k]["last_name"])
                print(f"student contact no : {k}",counsellor[k]["contact no"])
                print(f"student subject : {k}",counsellor[k]['subject'])
                print(f"student fees : {k}",counsellor[k]['subject_fees'])
 
        for k in counsellor.keys():
                print("----------------------")
                print(f"subject : {k} ")
                print(f"subject fees : (for 1 time subject) ",counsellor[k]["fees"])

        subject = input("enter subject which you want to add : ")
            

        subject = subject_fees*subject[first_name]['fees']
        print("FEES =",'total fees')

        
    elif choice==3:
        for i in counsellor.keys():
            print("------------------------------------------")

