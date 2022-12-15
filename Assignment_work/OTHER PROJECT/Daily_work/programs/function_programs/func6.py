#function with parameter and function with return type
#syntax:
#def funname(parameter)
#}
    #return statment
#{

def menu():
    data = """
                            MENU

                    press 1 for addtion
                    press 2 for multiplication   
    
            """
    print(data)

    choice = int(input("enter your choice:"))

    num1 = int(input("enter a number1:"))
    num2 = int(input("enter a number2:"))
    if choice == 1:
        print(addition(num1,num2))
    elif choice==2:
      print(mul(num1,num2))
    else:
        print("invalid input")


def addition(n1,n2):
    ans = n1+n2
    return ans

def mul(n1,n2):
    ans = n1*n2
    return ans


menu()
