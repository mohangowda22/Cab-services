import sqlite3 as sql

def createDriverDb():
    conn=sql.connect("cabServices_db.db")
    sqlQuery="create table if not exists driver(name char(100),phone char(12),email char(30),d_password char(100),primary key(phone))"
    conn.execute(sqlQuery)

def compPassword():
    password=input("Enter Password:")
    cpassword=input("Repeate Password:")
    if(password==cpassword):
        return password
    else:
        print("Both password did not match\nPlease enter the password once again..\n")

def regDriver():
    driverName=input("\nEnter your name:")
    driverPhone=int(input("Enter a vaild Phone Number:"))
    driverEmailid=input("Enter your E-mail ID:")
    driverPassword=compPassword()
    conn=sql.connect("cabServices_db.db")
    query_regDriver="insert into driver values(?,?,?,?)"
    conn.execute(query_regDriver,(driverName,driverPhone,driverEmailid,driverPassword))
    conn.commit()
    print("Registred as Driver..")
    input()

def loginDriver():
    driverPhone=int(input("Enter your Registred Phone number:"))
    driverPassword=input("Enter the password:")
    conn=sql.connect("cabServices_db.db")
    cur=conn.cursor()
    query_loginDriver="select phone,d_password from driver"
    cur.execute(query_loginDriver)
    dataList=cur.fetchall()
    flag=False
    for data in dataList:
        if(int(data[0])==driverPhone and data[1]==driverPassword):
            flag=True
        else:
            flag=False
    if(flag==True):
        print("User vaild")
        input()
        #call wait for booike
    else:
        print("Login Failed..\nCheck your Phone number and password\nTry again..\n")
        loginDriver()

def displayChoice():
    print("\n\tWelcome to Cab services\nPlease select your choice..\n")
    choice=int(input("1:Login\n2:Sign-Up\n\nEnter your choice:"))
    if(choice==1):
        loginDriver()
        input()
        displayChoice()
    elif(choice==2):
        regDriver()
        input()
        displayChoice()
    elif(ch==3):
        print("Quiting..")
        exit()
    else:
        print("Please enter a valid choice..\nTry again")
        displayChoice()
