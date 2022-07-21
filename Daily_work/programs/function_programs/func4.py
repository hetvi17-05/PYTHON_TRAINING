#function with parameter and function without return type.
#syntax:
        #def  <function>( ):
            #statment
def sum(num1,num2):
    print(num1)
    print(num2)

    ans = num1+num2
    print(ans)

num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))
 
sum(num1,num2)