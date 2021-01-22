import tkinter
from tkinter import *
import mysql.connector

window=Tk()
window.geometry("500x300")
window.title("Lifechoices online""Login")
'''<!---------------------------------->'''
import time

time1 = ''
clock = Label(window, font=('times', 15, 'bold'), )

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()




def admin_detail():
    import mysql.connector
    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )

    mycursor=mydb.cursor()
    xy=mycursor.execute("select * from user")
    for i in mycursor:
        print(i)

def sign_up():
    import mysql.connector
    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )

    mycursor=mydb.cursor()

    sql="insert into user values(%s,%s,%s,%s,%s)"
    val=('0',e_name.get(),'default',e_pass.get(),"test")
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inseted.')
    xy=mycursor.execute('select * from user')
    for i in mycursor:
        print(i)




'''<!----------------------------------------------->'''








clock.pack(fill=BOTH, )

frlbl_name = LabelFrame(window, text='Full Name',font=('times', 20, 'bold'))
frlbl_name.pack(fill="both", expand="yes")


e_name = Entry(frlbl_name, )
e_name.config(width=20,)
e_name.pack(ipady=3)



frlbl_pass = LabelFrame(window, text='Password',font=('times', 20, 'bold'),)
frlbl_pass.pack(fill="both", expand="yes")
e_pass = Entry(frlbl_pass, )
e_pass.config(width=20,show='*')
e_pass.pack(ipady=3)

b_signin=Button(window,text="Sign-Up",command=sign_up)
b_signin.config(height=3,width=10)
b_signin.pack()

window.mainloop()
