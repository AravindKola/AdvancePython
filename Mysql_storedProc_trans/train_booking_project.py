from threading import Thread, Lock
from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection,Thread):
    def available_seats(self):
        try:
            global mydata
            global seats
            mydata=(int(input("Enter train number:")),)
            self.cursor.callproc("get_seats",args=mydata)
            for r in self.cursor.stored_results():
                print("no of seats available:",end="")
                seats=r.fetchone()[0]
                print(seats)
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def run(self):
        l = Lock()
        l.acquire()
        import mysql.connector
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hcl_vijayawada")
            cursor=conn.cursor()
            name=input("Enter name")
            age=int(input("Enter age"))
            tkts=int(input("Number of tickets"))
            sql="insert into customer_details(cust_name,age,no_of_tkts) values(%s,%s,%s);"
            tuple1=(name,age,tkts)
            cursor.execute(sql,tuple1)
            sql1="select * from trains where train_no=%s;"
            sql2="select * from customer_details where cust_name='{0}'".format(name)
            cursor.execute(sql1,mydata)
            row=cursor.fetchone()[2]
            a=float(row)
            print(row)
            cursor.execute(sql2)
            row1 = cursor.fetchone()[3]
            b=float(row1)
            print(row1)
            amt=a*b
            print("TOATAL AMOUNT:",amt)
            cursor.execute(sql1,mydata)
            row3=cursor.fetchone()[1]
            row3=row3-b
            row3=int(row3)
            sql3="update trains set no_of_seats=%s;"
            cursor.execute(sql3,(row3,))
            print("No.of seats still available:", row3)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
            l.release()

ob=Booking()
ob.connect("localhost","root","root","hcl_vijayawada")
ob.available_seats()
ob.start()
