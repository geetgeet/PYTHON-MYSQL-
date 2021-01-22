
'''def admin_detail():
    import mysql.connector
    mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )

    mycursor=mydb.cursor()
    xy=mycursor.execute("select * from user")
    for i in mycursor:
        print(i)


admin_detail()
'''





'''<!-----------------shows user details------------------------------------>'''

import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )

mycursor=mydb.cursor()
xy=mycursor.execute("select * from user")
for i in mycursor:
    print(i)
    
 # <!------------------------------------------------------->


'''def add_user():
    mycursor=mydb.cursor()

    sql="insert into user values(%s,%s,%s,%s)"
    val=('0000','User Att1','default','12345')
    mycursor.execute(sql,val)
    mydb.commit()
print(mycursor.rowcount,'record inseted.')
xy=mycursor.execute('select * from user')
for i in mycursor:
    print(i)
'''



'''<!----------------Some kind of edit function--------------------->'''
'''

#Dentist code works here
import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='hospital',
                             auth_plugin='mysql_native_password'
                             )
mycursor=mydb.cursor()
sql="UPDATE Dentists SET Dentist_surname = 'thisupdated' WHERE Dentist_name = 'gabe'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
xy=mycursor.execute('select * from Dentists')
for i in mycursor:
    print(i)
    
    
<!-------------------------------------------------------------------->
'''



'''<!---------------------Count Show (amount)------------------------------------->'''
'''
import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )
mycursor=mydb.cursor()

xy=mycursor.execute('SELECT count(*) from user')
for i in mycursor:
    print("There are {} records".format(i))

#<--------------------------------------------------------------->
'''

'''<--------Show Privileges------------------------------->'''
'''
import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )
mycursor=mydb.cursor()

xy=mycursor.execute('Show privileges')
for i in mycursor:import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )
mycursor=mydb.cursor()

sql="insert into user values(%s,%s,%s,%s,%s)"
val=('0','aaa','username','password','student')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'record inseted.')
xy=mycursor.execute('select * from user')
for i in mycursor:
    print(i)
    
    print(i)

<---------------------------------------------------------->
'''

'''<!--------------Insert Function------------------>'''

''''
import mysql.connector
mydb=mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',
                             host='127.0.0.1',database='lifechoicesonline',
                             auth_plugin='mysql_native_password'
                             )
mycursor=mydb.cursor()

sql="insert into user values(%s,%s,%s,%s,%s)"
val=('0','aaa','username','password','student')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'record inseted.')
xy=mycursor.execute('select * from user')
for i in mycursor:
    print(i)
    
    
#<-------------------------------------------------->#
'''
