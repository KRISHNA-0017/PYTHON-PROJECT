import pandas as pd
from tabulate import tabulate
import mysql.connector as sqlt
import matplotlib.pyplot as plt
con=sqlt.connect(host = "localhost", user = "root", passwd="shrikrishna17#", database = "inventory")
cursor=con.cursor()
def purchase():
     try:
          pid=0
          total=0
          grand=0
          l=[]
          ch='y'
          q="select max(pid) as largest from purchase"
          cursor.execute(q)
          r=cursor.fetchone()[0]
          if r:
              pid=r+1
          else:
              pid=1
          pdate=input("Enter Purchase date : ")
          sid = int(input("Enter Supplier ID : "))
          q1="select * from Supplier where sid = {};".format(sid)
          cursor.execute(q1)
          if cursor.fetchone():
              df=pd.read_sql(q1,con)
              print(tabulate(df,headers="keys", tablefmt = "psql", showindex = False)) 
              print("Item Details.....")
              df1=pd.read_sql("select * from item",con)
              print(tabulate(df1,headers='keys',tablefmt='psql',showindex=False))
              while(ch=='y'):
                  ino=int(input("Enter Item No : "))
                  cursor.execute("select * from item where ino ={};".format(ino))
                  r1=cursor.fetchone()
                  if r1:
                      qty = int(input("Enter qty : "))
                      rate=r1[2]
                      total=qty*rate
                      grand=grand+total
                      t=(pid,ino,qty,rate,total)
                      l.append(t)
                  else:
                      print("Item Not Found")
                  ch=input("Do you wish to add more Items in bucket y/n : ")
              q2="insert into purchase values({},'{}',{},{});".format(pid,pdate,sid,grand)
              cursor.execute(q2)
              con.commit()
              q3="insert into pdetails values(%s,%s,%s,%s,%s);"
              cursor.executemany(q3,l)
              con.commit()
              cursor.executemany("insert into ptemp values(%s,%s,%s,%s,%s);",l)
              con.commit()
              q4="update item join ptemp using(ino) set item.qty = item.qty+ptemp.pqty"
              cursor.execute(q4)
              con.commit()
              cursor.execute("delete from ptemp")
              con.commit()
              print("Item Purchased and Added")
          else:
              print("Supplier Not Found")
     except:
         print("Wrong Entry..Please check")
def sale():
     try:
           saleid=0
           total=0
           grand=0
           l=[]
           ch='y'
           q="select max(saleid) as largest from sales"
           cursor.execute(q)
           r=cursor.fetchone()[0]
           if r:
                saleid=r+1
           else:
                saleid=1
           sdate=input("Enter Sale date : ")
           cid = int(input("Enter Customer ID : "))
           q1="select * from customer where cid = {};".format(cid)
           cursor.execute(q1)
           if cursor.fetchone():
                df=pd.read_sql(q1,con)
                print(tabulate(df,headers="keys", tablefmt = "psql", showindex = False))
                print("Item Details")
                df1=pd.read_sql("select * from item",con)
                print(tabulate(df1,headers='keys',tablefmt='psql',showindex=False))
                while(ch=='y'):
                     ino=int(input("Enter Item No : "))
                     cursor.execute("select * from item where ino ={};".format(ino))
                     r1=cursor.fetchone()
                     if r1:
                          qty = int(input("Enter qty : "))
                          rate=r1[3]
                          total=qty*rate
                          grand=grand+total
                          t=(saleid,ino,qty,rate,total)
                          l.append(t)
                     else:
                          print("Item Not Found")
                     ch=input("Do you wish to add more Items in bucket y/n : ")
                q2="insert into sales values({},'{}',{},{});".format(saleid,sdate,cid,grand)
                cursor.execute(q2)
                con.commit()
                q3="insert into sdetails values(%s,%s,%s,%s,%s);"
                cursor.executemany(q3,l)
                con.commit()
                cursor.executemany("insert into stemp values(%s,%s,%s,%s,%s);",l)
                con.commit()
                q4="update item join stemp using(ino) set item.qty = item.qty-stemp.sqty"
                cursor.execute(q4)
                con.commit()
                cursor.execute("delete from stemp")
                con.commit()
                print("Item Saled and Updated")
           else:
                print("Customer Not Found")
     except:
         print("Wrong Entry..Please check")

