def menu():
    data = """
                    MENU

            press 1 for addition 
            press 2 for multiplication
    
    """
    print(data)
    choice = int(input("enter your choice:"))
    if choice==1:
        addtion()
    elif choice==2:
        mul()

def addtion():
    num1 = int(input("enter a number 1 :"))
    num2 = int(input("enter a number 2 :"))
    ans = num1 + num2
    print(ans)

def mul():
    num1 = int(input("enter a number 1 :"))
    num2 = int(input("enter a number 2 :"))
    ans = num1 + num2
    print(ans)

status= True
while status:
    menu()
    choice = input("do you want to continue? press 'y' for yes and 'n' for no")
    if choice=='n' or choice=='no':
        status = False