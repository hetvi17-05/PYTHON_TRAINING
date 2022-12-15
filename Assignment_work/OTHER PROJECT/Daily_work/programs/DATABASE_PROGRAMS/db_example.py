#import pymysql
from tkinter import Entry, Label, Tk

#mydb = pymysql.connect(host="localhost",user="root",password="",database="python_db1")

#cur = mydb.cursor()

#cur.execute ("create table if not exists student (id int primary key AUTO_INCREMENT ,name varchar(20),subject varchar(20))")

#mydb.commit()

screen = Tk()
screen.geometry("500x500")

lbl_name = Label(screen,text="Enter Name :")
lbl_name.place(x=10,y=10)

lbl_subject = Label(screen,text="Enter Subject :")
lbl_subject.place(x=10,y=60)


ename = Entry(screen)
ename.place(x=150,y=60)

esubject = Entry(screen)
esubject.place(x=150,y=60)

screen.mainloop()