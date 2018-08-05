import BookClass
import sqlite3 as sql
import random as rnd


def retriveDrivers():
    conn=sql.connect("cabServices_db.db")
    cur=conn.cursor()
    queryReteiveDrivers="select name,phone,rate from driver"
    cur.execute(queryReteiveDrivers)
    driversData=cur.fetchall()
    cur.close()
    #print(len(driversData))
    return driversData

def chooseDriver(customerName,customerPhone,distanceToDestination):
    driversData=retriveDrivers()
    numDrivers=len(driversData)
    select=rnd.randint(0,numDrivers-1)
    print("Selected:",select)
    obj_bookie=BookClass.Booking()
    for i in range(len(driversData)):
        if(i==select):
            obj_bookie.d_name=driversData[i][0]
            obj_bookie.d_phone=driversData[i][1]
            obj_bookie.c_name=customerName
            obj_bookie.c_phone=customerPhone
            obj_bookie.travelCost=(driversData[i][2]*distanceToDestination)
            return obj_bookie
            #print(obj_bookie.d_name)
#chooseDriver("mohan","345",23)
