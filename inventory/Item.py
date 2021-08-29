import pandas as pd
from tabulate import tabulate
import mysql.connector as sqlt
import matplotlib.pyplot as plt
con=sqlt.connect(host = "localhost", user = "root", passwd="shrikrishna17#", database = "inventory")
cursor=con.cursor()
def add_item():
    try:
         ino = int(input("Enter Item No : "))
         iname = input("Enter Iname : ")
         prate=float(input("Enter Purchase Rate : "))
         srate=float(input("Enter Sale Rate : "))
         qty=int(input("Enter Qty On Hand : "))
         q="insert into item values({},'{}',{},{},{});".format(ino,iname,prate,srate,qty)
         cursor.execute(q)
         con.commit()
         print("Item Added")
    except:
         print("Wrong Entry..Please check")
def edit_item():
    try:
         ino=int(input("Enter Item No : "))
         q="select * from item where ino = {};".format(ino)
         cursor.execute(q)
         if cursor.fetchone():
             iname=input("Enter Item Name : ")
             cursor.execute("update item set iname = '{}' where ino={};".format(iname,ino))
             qty=int(input("Enter Qty On Hand : "))
             cursor.execute("update item set qty = '{}' where ino={};".format(qty,ino))
             con.commit()
             print("item Edited")
         else:
             print("Item Not Found")
    except:
         print("Wrong Entry")
def fix_rate():
    try:
         ino=int(input("Enter Item No : "))
         q="select * from item where ino = {};".format(ino)
         cursor.execute(q)
         if cursor.fetchone():
             prate=int(input("Enter new purchase rate : "))
             srate=int(input("Enter new Sale rate : "))
             cursor.execute("update item set prate={},srate={} where ino={};".format(prate,srate,ino))
             con.commit()
             print("New rate applied")
         else:
             print("Item Not Found")
    except:
         print("Wrong Entry")
def search_item():
    try:
         ino=int(input("Enter Item No : "))
         q="select * from item where ino = {};".format(ino)
         cursor.execute(q)
         if cursor.fetchone():
             df=pd.read_sql(q,con)
             print(tabulate(df,headers="keys", tablefmt = "psql", showindex = False))
         else:
             print("Item Not Found")
    except:
         print("Wrong Entry")
def delete_item():
    try:
         ino=int(input("Enter Item No : "))
         q="select * from item where ino = {};".format(ino)
         cursor.execute(q)
         if cursor.fetchone():
             cursor.execute("delete from item where ino={};".format(ino))
             con.commit()
             print("item deleted")
         else:
             print("Item Not Found")
    except:
         print("Wrong Entry")         
def display_item():
     df=pd.read_sql("select * from item",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
         
