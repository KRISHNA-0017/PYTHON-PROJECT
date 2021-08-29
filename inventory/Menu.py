import Item
import Customer
import Supplier
import Transaction
import report
while(True):
   print("\nENTER YOUR CHOICE : \n1.ITEMS\n2.CUSTOMERS\n3.SUPPLIERS\n4.TRANSACTION\n5.REPORT\n6.EXIT")
   ch=int(input())
   if ch==1:
     while(True):
         print("\nENTER YOUR CHOICE : \n1.ADD ITEM\n2.EDIT ITEM\n3.FIX RATE\n4.SEARCH ITEM\n5.DELETE\n6.DISPLAY ITEM\n7.Exit")
         ch=int(input())
         if ch==1:
             Item.add_item()
         elif ch==2:
             Item.edit_item()
         elif ch==3:
             Item.fix_rate()
         elif ch==4:
             Item.search_item()
         elif ch==5:
             Item.delete_item()
         elif ch==6:
             Item.display_item()
         elif ch==7:
             break
   elif ch==2:
     while(True):
         print("\nENTER YOUR CHOICE\n1.ADD CUSTOMERS\n2.EDIT CUSTOMERS\n3.SEARCH CUSTOMERS\n4.DELETE CUSTOMERS\n5.DISPLAY CUSTOMERS\n6.EXIT")
         ch=int(input())
         if ch==1:
             Customer.add_customer()
         elif ch==2:
             Customer.edit_customer()
         elif ch==3:
             Customer.search_customer()
         elif ch==4:
             Customer.delete_customer()
         elif ch==5:
             Customer.display_customer()
         elif ch==6:
             break
   elif ch==3:
     while(True):
         print("\nENTER YOUR CHOICE\n1.ADD SUPPLIERS\n2.EDIT SUPPLIERS\n3.SEARCH SUPPLIERS\n4.DELETE SUPPLIERS\n5.DISPLAY SUPPLIERS\n6.EXIT")
         ch=int(input())
         if ch==1:
             Supplier.add_supplier()
         elif ch==2:
             Supplier.edit_supplier()
         elif ch==3:
             Supplier.search_supplier()
         elif ch==4:
             Supplier.delete_supplier()
         elif ch==5:
             Supplier.display_supplier()
         elif ch==6:
             break
   elif ch==4:
     while(True):
         print("\nENTER YOUR CHOICE \n1.SALE\n2.PURCHASE\n3.exit")
         ch=int(input())
         if ch==1:
             Transaction.sale()
         elif ch==2:
             Transaction.purchase()
         elif ch==3:
             break
   elif ch==5:
     while(True):
         print("\nENTER YOUR CHOICE \n1.ITEM DETAILS\n2.CUSTOMER DETAILS\n3.SUPPLIER DETAILS\n4.SALE DETAILS\n5.PURCHASE DETAILS\n6.EXIT")
         ch=int(input())
         if ch==1:
             report.show_item()
         elif ch==2:
             report.show_customer()
         elif ch==3:
             report.show_supplier()
         elif ch==4:
             report.show_sale()
         elif ch==5:
             report.show_purchase()
         elif ch==6:
             break
   elif ch==6:
        break
 
          
