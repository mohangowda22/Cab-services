import sqlite3 as sql

def createCustomerDb():
    conn=sql.connect("cabServices_db.db")
    sqlQuery="create table if not exists customer(name char(100),phone char(12),email char(30),c_password char(100),primary key(phone))"
    conn.execute(sqlQuery)

def compPassword():
    password=input("Enter Password:")
    cpassword=input("Repeate Password:")
    if(password==cpassword):
        return password
    else:
        print("Both password did not match\nPlease enter the password once again..\n")

def regCustomer():
    customerName=input("\nEnter your name:")
    customerPhone=int(input("Enter a vaild Phone Number:"))
    customerEmailid=input("Enter your E-mail ID:")
    customerPassword=compPassword()
    conn=sql.connect("cabServices_db.db")
    query_regCustomer="insert into customer values(?,?,?,?)"
    conn.execute(query_regCustomer,(customerName,customerPhone,customerEmailid,customerPassword))
    conn.commit()
    print("Registred as Customer..")
    input()

def loginCustomer():
    customerPhone=int(input("Enter your Registred Phone number:"))
    customerPassword=input("Enter the password:")
    conn=sql.connect("cabServices_db.db")
    cur=conn.cursor()
    query_loginCustomer="select phone,c_password from customer"
    cur.execute(query_loginCustomer)
    dataList=cur.fetchall()
    flag=False
    for data in dataList:
        if(int(data[0])==customerPhone and data[1]==customerPassword):
            flag=True
        else:
            flag=False
    if(flag==True):
        print("User vaild")
        input()
        #call for book cabs
    else:
        print("Login Failed..\nCheck your Phone number and password\nTry again..\n")
        loginCustomer()

def displayChoice():
    print("\n\tWelcome to Cab services\nPlease select your choice..\n")
    choice=int(input("1:Login\n2:Sign-Up\n\nEnter your choice:"))
    if(choice==1):
        loginCustomer()
        input()
        displayChoice()
    elif(choice==2):
        regCustomer()
        input()
        displayChoice()
    elif(ch==3):
        print("Quiting..")
        exit()
    else:
        print("Please enter a valid choice..\nTry again")
        displayChoice()
