


'''  mydb.commit()
    print(mycursor.rowcount,"record inserted.")
    xy=mycursor.execute('select * from user')
    for i in mycursor:
        print(list(i))

    lbl_disp=Label(window,)
    lbl_disp.pack()
    lbl_disp.configure(text=i)'''


import mysql.connector
import tkinter  as tk
from tkinter import *
my_connect =mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password')
my_cursor = my_connect.cursor()


'''----------------------functions-----------------------------------------------'''
def my_details(id):
    try:
        val = int(id) # check input is integer or not
        try:
            my_cursor.execute("SELECT * FROM user WHERE id="+id)
            rec = my_cursor.fetchall()
            print(rec)
            my_str.set(rec)

        except :
             my_str.set("Database error")
    except:
        my_str.set("Check input")





def del_r():
    id=t1.get('1.0',END)
    con = mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password')
    cur = con.cursor()
    cur.execute("DELETE FROM user WHERE id=%s", (id,))
    con.commit()
    con.close()

def add():
    my_w.withdraw()
    import Register_category


'''======================================================================'''
####### end of connection ####

my_w = tk.Tk()
my_w.geometry("800x500")
my_w.title("ADMIN")

# add one Label
l1 = tk.Label(my_w,  text='Enter ID:(in yellow) ', width=25 )
l1.pack()

# add one text box
t1 = tk.Text(my_w,  height=1, width=4,bg='yellow')
t1.pack()

b1 = tk.Button(my_w, text='Show Details of id', width=15,bg='white',
    command=lambda: my_details(t1.get('1.0',END)))
b1.configure()
b1.pack()
del_b = tk.Button(my_w, text='Delete User', width=15,bg='red',
    command=del_r)
del_b.configure()
del_b.pack()
del_b = tk.Button(my_w, text='Add User', width=15,bg='lightgreen',
    command=add)
del_b.configure()
del_b.pack()

my_str = tk.StringVar()

# add one Label
l2 = tk.Label(my_w,  textvariable=my_str, width=30, )
l2.configure(width=100,background='pink')
l2.pack()

my_str.set("Output")

listBox = Listbox(my_w, width=70)
listBox.pack()




def populatebox():
    listBox.delete(0,"end")

    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='localhost',
                                   database='lifechoicesonline')
    mycursor = mydb.cursor()
    sql = "select id, username, password, sign_in from user"
    mycursor.execute(sql)
    for i in mycursor:
        listBox.insert("end", i)


def exit():
    my_w.withdraw()
    import Buttons

update_btn = Button(my_w, text="Show All",font=('times',12,'bold'), command=lambda: populatebox())
update_btn.config(height=2,width=8)
update_btn.pack()

exit_btn = Button(my_w, text="Exit",font=('times',12,'bold'), command=exit)
exit_btn.config(height=2,width=8)
exit_btn.pack()
my_w.mainloop()
