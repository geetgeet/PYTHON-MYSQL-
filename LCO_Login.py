import tkinter
from tkinter import *
from tkinter import messagebox

from datetime import datetime

window=Tk()
window.geometry("500x300")
window.title("Lifechoices online""Login")
import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )
mycursor=mydb.cursor()


'''<----------------CREATE FUNCTIONS------------------------------------------>'''

now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M:%S")

def verify():
    user_v=e_id.get()
    pass_v=e_pass.get()
    sql=" (select * from user where username=%s and password=%s)"
    mycursor.execute(sql,[(user_v),pass_v])
    res=mycursor.fetchall()
    if res:
        for i in res:
            logged()
            break
    else:
        messagebox.showerror("Error","Please Enter Valid User ")


d=datetime.now()
def logged():
    t=d.strftime("%H;%M")
    dt=d.strftime("%d/%m/%y")
    uCom1="update user set sign_in=%s,status=%s,sign_out=%s  where username=%s "
    infoU1=(d,'IN','NULL',e_id.get())
    mycursor.execute(uCom1,infoU1)
    mydb.commit()
    messagebox.showinfo('info',"successfully signed in")


def out():
    messagebox.showinfo("MESSAGE","YO ARE ABOUT TO SIGN OUT")
    do=datetime.now()
    t=d.strftime("%H;%M")
    dt=d.strftime("%d/%m/%y")
    uCom2="update user set sign_out=%s,status=%s, sign_in=%s where username=%s "
    infoU2=(do,'OUT','NULL',e_id.get())
    mycursor.execute(uCom2,infoU2)
    mydb.commit()





'''
    import mysql.connector
    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )

    mycursor=mydb.cursor()
  #  id_max=(mycursor.execute("select * from user"))
    sql="UPDATE user SET sign_in=%s WHERE password=%s "
    val=(str(time) )
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted.")
    xy=mycursor.execute('select * from user')
    for i in mycursor:
        print(i)'''



xy=mycursor.execute('SELECT count(*) from user')
for i in mycursor:
    print("There are {} records".format(i))
'''<-------------------END OF FUNCTIONS----------------------------------------------------->'''
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


clock.pack(fill=BOTH, )

frlbl_id = LabelFrame(window, text='Name',font=('times', 20, 'bold'))
frlbl_id.pack(fill="both", expand="yes")


e_id = Entry(frlbl_id )
e_id.config(width=20,)
e_id.pack(ipady=3)
frlbl_pass = LabelFrame(window, text='Password',font=('times', 20, 'bold'),)

frlbl_pass.pack(fill="both", expand="yes")

e_pass = Entry(frlbl_pass, )
e_pass.config(width=20,show='*')
e_pass.pack(ipady=3)

b_signin=Button(window,text="Sign-In",command=verify)
b_signin.config(height=3,width=10)
b_signin.pack()


btnOut=Button(window,text="out",command=out)
btnOut.config(height=3,width=10)
btnOut.pack()

window.mainloop()

