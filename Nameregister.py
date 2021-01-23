import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime
now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M:%S")
print(str(time))
do=datetime.now()



'''<------------------Creating Functions------------------------>'''


def register_name_update():
        name=e_id.get()
        username=e_username.get()
        password=e_password.get()
        import mysql.connector
        mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )

        mycursor=mydb.cursor()
  #  id_max=(mycursor.execute("select * from user"))
        sql="UPDATE user SET full_name = %s, username=%s, password= %s,status=%s,mobile_number=%s, date_joined=%s WHERE full_name ='' "
        val=(str(e_id.get()),str(e_username.get()),str(e_password.get()),'IN',str(e_number.get()),now)
        if name=='' or username=='' or password=='':
            messagebox.showerror("Error"," Enter ALL fields ")


        else:

            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount,"record inserted.")
            xy=mycursor.execute('select * from user')
            messagebox.showinfo('Message',"User Added")
            window.withdraw()
            import Buttons



            for i in mycursor:
                print(i)











'''<-------------------End of functions------------------------->'''


window=Tk()
window.geometry("500x300")
window.title("Lifechoices online""Register")

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

frlbl_id = LabelFrame(window, text='Full Name',font=('times', 20, 'bold'))
frlbl_id.pack(fill="both", expand="yes")
e_id = Entry(frlbl_id)
e_id.config(width=20,)
e_id.pack(ipady=3)


frlbl_username = LabelFrame(window, text='Username',font=('times', 20, 'bold'))
frlbl_username.pack(fill="both", expand="yes")
e_username = Entry(frlbl_username)
e_username.config(width=20,)
e_username.pack(ipady=3)


frlbl_password = LabelFrame(window, text='Password',font=('times', 20, 'bold'),)
frlbl_password.pack(fill="both", expand="yes")
e_password = Entry(frlbl_password )
e_password.config(width=20,show='*')
e_password.pack(ipady=3)

frlbl_number = LabelFrame(window, text='Mobile number',font=('times', 20, 'bold'),)
frlbl_number.pack(fill="both", expand="yes")
e_number = Entry(frlbl_number )
e_number.config(width=20,show='*')
e_number.pack(ipady=3)

b_signin=Button(window,text="Sign-Up",command=register_name_update)
b_signin.config(height=3,width=10)
b_signin.pack()

window.mainloop()

