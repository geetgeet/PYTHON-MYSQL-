import tkinter
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('SIGN IN')


window.geometry("500x300")
window.configure(bg="teal")

#messagebox._show("Sign In","You are about to Sign in")

"CreatiNg Functions"

def register():
    window.withdraw()
    import Register_category



def student():
    window.withdraw()
    import LCO_Login

def staff():
    window.withdraw()
    import LCO_Login


def visitor():
    window.withdraw()
    import LCO_Login
def admin():
    messagebox.showinfo("info","Use hotkey")




lbl_instruc=Label(window,text="[SELECT CATEGORY] \n Sign In As:",font=('times', 20, 'bold'))
lbl_instruc.pack()

b_visitors=Button(window,text="Sign-IN",command=visitor,font=('times',12,'bold'))
b_visitors.config(height=3,width=10)


b_register=Button(window,text="Create New",command=register)
b_register.config(height=2,width=10,)

b_admin=Button(window,text="Admin",command=admin)
b_admin.config(height=3,width=10)



#Packing widgets

b_register.pack()

b_visitors.pack()
b_admin.pack()
def h_admin():
    window.withdraw()
    import Admin

def hotkey():
    h_admin()

window.bind("<Control-a>",lambda x:hotkey())

window.mainloop()

