year = int(input("enter a year: "))
if (year % 400 == 0)and (year % 100 == 0):
    print(year, "is a leap year")
elif(year % 4 == 0)and(year % 100 !=0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

"""from random import shuffle
x = ['kp','sh']
shuffle(x)
print(x)"""
"""
from datetime import date

today = date.today()
print("current year",today.year)
print("current month",today.month)
print("current day",today.day)"""
