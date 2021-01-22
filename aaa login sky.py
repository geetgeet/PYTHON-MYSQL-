import tkinter as tk
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(user='lifechoices',password='@Lifechoices1234', host='127.0.0.1', database='lifechoicesonline',auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

root=tk.Tk()
root.title("My logs")
root.geometry("400x400")

lbluser=tk.Label(root, text="please enter username")
lbluser.place(x=50, y=20)
username=tk.Entry(root, width=45)
username.place(x=250, y=20, width=100)
lblpassword= tk.Label(root,text="please enter password")
lblpassword.place(x=50, y=50)
password = tk.Entry(root,width=35)
password.place(x=250, y=50, width=100)
Loginbtn = tk.Button(root, text="Login", bg='Magenta' , command="verify")
Loginbtn.place(x=150, y=135 , width=55)
Registrationbtn = tk.Button(root, text="Register new user" , bg='Magenta', command="verify")
Registrationbtn.place(x=250, y=135, width=150)

def verify():
    user_verification = username.get()
    pass_verification = password.get()
    sql = "select * from user where user = %s and password = %s"
    mycursor.execute(sql, [(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break

    else:
        failed()

def logged():
    messagebox.showinfo("you have successfully logged in")

def failed():
    messagebox.showinfo("failed to log in")




root.mainloop()
