import pandas as pd
from tabulate import tabulate
import mysql.connector as sqlt
import matplotlib.pyplot as plt
con=sqlt.connect(host = "localhost", user = "root", passwd="shrikrishna17#", database = "inventory")
cursor=con.cursor()
def add_supplier():
     try:
          sid = int(input("Enter Supplier ID : "))
          sname = input("Enter Supplier Name : ")
          sadd=input("Enter Address : ")
          mobile=input("Enter Mobile : ")
          q="insert into supplier values({},'{}','{}','{}');".format(sid,sname,sadd,mobile)
          cursor.execute(q)
          con.commit()
          print("Supplier Added")
     except:
         print("Wrong Entry..Please check")
def edit_supplier():
     try:
          sid=int(input("Enter Supplier ID : "))
          q="select * from Supplier where sid = {};".format(sid)
          cursor.execute(q)
          if cursor.fetchone():
              sname = input("Enter Supplier Name : ")
              cursor.execute("update Supplier set sname = '{}' where sid={};".format(sname,sid))
              sdd=input("Enter Supplier Address : ")
              cursor.execute("update Supplier set sdd = '{}' where sid={};".format(sdd,sid))
              mobile=input("Enter Mobile : ")
              cursor.execute("update Supplier set mobile = '{}' where sid={};".format(mobile,sid))
              con.commit()
              print("Supplier Edited")
          else:
              print("Supplier Not Found")
     except:
         print("Wrong Entry..Please check")
def search_supplier():
     try:
          sname=input("Enter Supplier Name : ")
          q="select * from supplier where sname like '%{}%';".format(sname)
          cursor.execute(q)
          if cursor.fetchall():
              df=pd.read_sql(q,con)
              print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
          else:
              print("Supplier Not found")
     except:
         print("Wrong Entry..Please check")
def delete_supplier():
     try:
          sid=int(input("Enter Supplier ID"))
          q="select * from supplier where sid = {};".format(sid)
          cursor.execute(q)
          if cursor.fetchone():
              cursor.execute("delete from supplier where sid={};".format(sid))
              con.commit()
              print("Supplier deleted")
          else:
              print("Supplier Not Found")
     except:
         print("Wrong Entry..Please check")
def display_supplier():
     df=pd.read_sql("select * from supplier",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))

