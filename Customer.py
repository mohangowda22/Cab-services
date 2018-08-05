import sqlite3 as sql
import BookCab

def createCustomerDb():
    conn=sql.connect("cabServices_db.db")
    sqlQuery="create table if not exists customer(name char(100),phone char(12),email char(30),c_password char(100),primary key(phone));"
    conn.execute(sqlQuery)
    conn.commit()
    conn.close()

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

def book(customerName,customerPhone):
    driverDetails=BookCab.chooseDriver(customerName,customerPhone,int(input("\nEnter the distance to travel:")))
    input()
    print("The Driver Details are:\n")
    print("Name of Driver:",driverDetails.d_name)
    print("Name of Driver:",driverDetails.d_phone)
    print("Total Esrimated cost:",driverDetails.travelCost)

def loginCustomer():
    customerPhone=int(input("Enter your Registred Phone number:"))
    customerPassword=input("Enter the password:")
    conn=sql.connect("cabServices_db.db")
    cur=conn.cursor()
    query_loginCustomer="select name,phone,c_password from customer"
    cur.execute(query_loginCustomer)
    dataList=cur.fetchall()
    flag=False
    for data in dataList:
        if(int(data[1])==customerPhone and data[2]==customerPassword):
            flag=True
            customerName=data[0]
        else:
            flag=False
    if(flag==True):
        while(True):
            book(customerName,customerPhone)
            c=input("Please confirm your ride:[y//n]:")
            if(c=="y" or c=="Y"):
                input("\nPress enter when ur trip ends..")
                break
            else:
                print("Select another press enter to continue..\n")
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
