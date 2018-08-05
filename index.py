import Customer
import Driver
Customer.createCustomerDb()
Driver.createDriverDb()
def startApp():
    print("*****WELCOME*****")
    print("\n\t1:Customer\n\t2:Driver\n\t3:Exit")
    ch=int(input("\nEnter your choice:"))
    if(ch==1):
        Customer.displayChoice()
        input()
        startApp()
    elif(ch==2):
        Driver.displayChoice()
        input()
        startApp()
    elif(ch==3):
        print("Thank you....\n")
        exit()
    else:
        print("Wrong input...!\nPlease Select a valid choice")
        startApp()

startApp()
