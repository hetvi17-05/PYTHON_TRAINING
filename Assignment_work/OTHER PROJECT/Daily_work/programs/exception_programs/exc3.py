#try : which contain error block
#except : which call when errors occurs
#finally : it always execute exception call or not
#else: it always execute when there is no exception



#try : which contain error block
try:
    num1 = int(input("enter a number:"))
    num2 = int(input("enter a number:"))

    ans = num1/num2

    print(ans)

#except : which call when errors occurs
except ZeroDivisionError:
    print("make sure entered number is greater than 0 ")
except:
    print("invalid input")



#else: it always execute when there is no exception
else:
    print(ans)

#finally : it always execute exception call or not
finally:
    print("THANK YOU FOR USING THIS APP")