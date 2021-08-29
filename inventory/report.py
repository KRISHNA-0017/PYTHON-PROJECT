import pandas as pd
from tabulate import tabulate
import mysql.connector as sqlt
import matplotlib.pyplot as plt
con=sqlt.connect(host = "localhost", user = "root", passwd="shrikrishna17#", database = "inventory")
cursor = con.cursor()
def show_item():
     df=pd.read_sql("select * from item",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
def show_customer():
     df=pd.read_sql("select * from customer",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
def show_supplier():
     df=pd.read_sql("select * from supplier",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
def show_sale():
     bdate=input("Enter beginning date : ")
     edate=input("Enter end date : ")
     df=pd.read_sql("select * from sales where sdate between '{}' and '{}';".format(bdate,edate),con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
     df=pd.read_sql("select * from sdetails",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
def show_purchase():
     bdate=input("Enter beginning date : ")
     edate=input("Enter end date : ")
     df=pd.read_sql("select * from purchase where pdate between '{}' and '{}';".format(bdate,edate),con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
     df=pd.read_sql("select * from pdetails",con)
     print(tabulate(df,headers= 'keys', tablefmt='psql',showindex = False))
