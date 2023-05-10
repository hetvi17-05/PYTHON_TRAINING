#remove duplicate 
num = [1,1,1,2,2,2,3,3,4,4,5,5]
new_num = []
for i in num:
    if i not in new_num:
        new_num.append(i)
print(new_num)

#find weekend of the year which comes friday
import calendar
import datetime
date = 13
year = 2023
day = 5
for i in range (1,13):
    dt = datetime.date(year,i,13)
    a = calendar.day_name[dt.weekday(5)]
if i in calendar:
    print("day",a)
else:
    print("not")
