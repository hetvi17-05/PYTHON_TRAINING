#nested_if_statment
# E.G.

email = "a@gmail.com"
password = "123456789"

s_email = input("enter email:")
s_password = input("enter password:")
if s_email==email:
    if s_password==password:
        print("welcome to tops technology")
    else:
        print("invalid password")
else:
    print("invalid email")