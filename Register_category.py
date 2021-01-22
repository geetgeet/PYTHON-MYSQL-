import tkinter
from tkinter import *
window=Tk()
window.title('Register Select')


window.geometry("500x300")
window.configure(bg="teal")

"Creating Functions"



def student():
    import mysql.connector

    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    sql="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=('0','','','','student','','','','','')

    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inseted.')
    xy=mycursor.execute('select * from user')
    for i in mycursor:
        print(i)

    window.withdraw()
    import Nameregister


def staff():
    import mysql.connector
    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    sql="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=('0','','','','staff','','','','','')
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inseted.')
    xy=mycursor.execute('select * from user')
    for i in mycursor:
        print(i)


    window.withdraw()
    import Nameregister



def visitor():
    import mysql.connector
    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    sql="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=('0','','','','visitor','','','','','')
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inseted.')
    xy=mycursor.execute('select * from user')
    for i in mycursor:
        print(i)

    window.withdraw()
    import Nameregister


lbl_instruc=Label(window,text="SELECT CATEGORY:",font=('times', 20, 'bold'))
lbl_instruc.grid(row=0,column=2)

b_visitors=Button(window,text="Vistors",command=visitor)
b_visitors.config(height=3,width=10)

b_staff=Button(window,text="Staff",command=staff)
b_staff.config(height=3,width=10)

b_students=Button(window,text="Students",command=student)
b_students.config(height=3,width=10)

lbl_hold=Label(window,text="     ")
lbl_hold.config(height=3,width=10, bg="teal")


#Packing widgets

lbl_hold.grid(row=1,column=2,)
b_students.grid(row=2,column=1)
b_staff.grid(row=2,column=2)
b_visitors.grid(row=2,column=3)

window.mainloop()

