#string : collection of charecters
#string which is represent by double qoutation
#eg name = "python"

menu = """
            press 1 for play
            press 2 for exit

"""
print(menu)

print("--------------------------------")
#len(): inbuilt function which is return length of string

name = input("enter your name :")
print(len(name))
print("------------------------------")

#lowe(): lower is inbuilt method which covert enetrd string onto lowercase.

choice = input("do yoy want to enter more student perss 'y' for yes ")
if choice.lower()=='y':
    print("yes")
else:
    print("no")
print("------------------------------------")

#uppercase() : to convert charecters into uppercase

name = "python"
print(name.upper())
print("-------------------------------------")

#endswith(): endswith check the string ending charecters with parametes 
#need to add endswith()at suffix.

website = input("enter website name:")
if website.endswith(".com"):
    print("valid input")
else:
    print("invalid input")
print("----------------------------------------")

name = "welcome"
print(name.center(50))
print("-----------------------------------------")

name = "python"
print(name.capitalize())
print("-----------------------------------------------")

#isalpha(): to check entered string contain only charecters or not
#if yes then it will return true.
firstname = input("enter your first name:")
if firstname.isalpha():
    print("yes valid")
else:
    print("invalid input")
    print("-----------------------------------------")

#isdigit(): to check enetred string contain digit or not.
contactNumber = int(input("enter you number:")) 
#check enterd string contain digit or not if yes thn it will return true.
if contactNumber.isdigit():
    print("valid input")
else:
    print("invalid input")

    