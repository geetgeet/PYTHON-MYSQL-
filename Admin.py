import tkinter
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('SIGN IN')


window.geometry("500x300")
window.configure(bg="teal")

import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
data=0


for i in mycursor:
        data.configure(text=i)

lbl_disp=Label(window,text=data)
lbl_disp.pack()
window.mainloop()
