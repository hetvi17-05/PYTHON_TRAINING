score = 0

def increment():
    global score
    score +=50

def decrement():
    global score
    score -=50

def menu():
    data = """
                        MENU
                press 1 for increment
                press 2  for decrement
       """
    print(data)

    choice = int(input("enter your choice:"))
    if choice==1:
        increment()
    elif choice==2:
        decrement()
    print("score = ",score)

status = True
while status:
    menu()
    choice = input("do you want to continue press y for yes and n for no:")
    if choice =='n':
        status = False