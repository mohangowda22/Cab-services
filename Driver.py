import sqlite3 as sql

def createDriverDb():
    conn=sql.connect("cabServices_db.db")
    sqlQuery="create table if not exists driver(name char(100),phone char(12),rate int,email char(30),d_password char(100),primary key(phone))"
    conn.execute(sqlQuery)
    conn.commit()
    conn.close()
#createDriverDb()

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
    rate=int(input("Enter the rate per KM:"))
    driverEmailid=input("Enter your E-mail ID:")
    driverPassword=compPassword()
    conn=sql.connect("cabServices_db.db")
    query_regDriver="insert into driver values(?,?,?,?,?)"
    conn.execute(query_regDriver,(driverName,driverPhone,rate,driverEmailid,driverPassword))
    conn.commit()
    print("Registred as Driver..")
    input()


def displayChoice():
    print("\n\tWelcome to Cab services\nPlease select your choice..\n")
    choice=int(input("1:Sign-Up\n2:Exit\nEnter your choice:"))
    if(choice==1):
        regDriver()
        input()
        displayChoice()
    elif(choice==2):
        print("Quiting..")
    else:
        print("Please enter a valid choice..\nTry again")
        displayChoice()
