import pandas as pd
from tabulate import tabulate
import mysql.connector as sqlt
import matplotlib.pyplot as plt
con=sqlt.connect(host = "localhost", user = "root", passwd="shrikrishna17#", database = "inventory")
cursor=con.cursor()
def add_customer():
     try :
          cid = int(input("Enter Customer ID : "))
          cname = input("Enter Customer Name : ")
          cadd=input("Enter Address : ")
          mobile=input("Enter Mobile : ")
          q="insert into customer values({},'{}','{}','{}');".format(cid,cname,cadd,mobile)
          cursor.execute(q)
          con.commit()
          print("Customer Added")
     except:
         print("Wrong Entry..Please check")
def edit_customer():
     try :
          cid=int(input("Enter Customer ID : "))
          q="select * from Customer where cid = {};".format(cid)
          cursor.execute(q)
          if cursor.fetchone():
              cname=input("Enter Customer Name : ")
              cursor.execute("update customer set cname = '{}' where cid={};".format(cname,cid))
              cdd=input("Enter Customer Address : ")
              cursor.execute("update customer set cdd = '{}' where cid={};".format(cdd,cid))
              mobile=input("Enter Mobile : ")
              cursor.execute("update customer set mobile = '{}' where cid={};".format(mobile,cid))
              con.commit()
              print("Customer Edited")
          else:
              print("Customer Not Found")
     except:
         print("Wrong Entry..Please check")
def search_customer():
     try:
         cid=int(input("Enter Customer ID : "))
         q="select * from customer where cid = {};".format(cid)
         cursor.execute(q)
         if cursor.fetchone():
             df=pd.read_sql(q,con)
             print(tabulate(df,headers="keys", tablefmt = "psql", showindex = False))
         else:
             print("Customer Not Found")
     except:
         print("Wrong Entry")
def delete_customer():
     try:
          cid=int(input("Enter Customer ID : "))
          q="select * from customer where cid = {};".format(cid)
          cursor.execute(q)
          if cursor.fetchone():
              cursor.execute("delete from customer where cid={};".format(cid))
              con.commit()
              print("Customer deleted")
          else:
              print("Customer Not Found")
     except:
         print("Wrong Entry..Please check")
def display_customer():
     df=pd.read_sql("select * from customer",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))

