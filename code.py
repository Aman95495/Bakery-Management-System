
#    BAKERY    MANAGEMENT     SYSTEM    PROJECT


#  Importing Modules and Connecting To Mysql Database - "Bakery"
import datetime
import mysql.connector as mycon
connect = mycon.connect(host="localhost",user="root",password="root",database="Bakery")
cursor = connect.cursor()


# Checking The Connection
'''
if connect.is_connected():
    print("Sucessfully connected to mysql database")
'''

#  Creating tables in Mysql
'''
cursor.execute("CREATE TABLE Itemslist (product_id  int,product_name  varchar(30),product_quantity int,product_price  float)")
cursor.execute("CREATE TABLE Bill (Serial int, prod_name varchar(30), prod_quantity int, prod_unit_price float, price float)")
cursor.execute("CREATE TABLE Customer(Customer_ID   int  NOT NULL  AUTO_INCREMENT, Customer_name  varchar(30), Date_Time  datetime, Amount float,Mobile bigint,PRIMARY KEY (Customer_ID))")
connect.commit()
'''


# Owner Details
UserName = "Aman@123"
Password = 957954

 # Customer Detail
Name = ""
Mobile = 0000000000

    

#                                                                                                                           OWNERS  PAGES
#####################################################################################################################



# Sixth Page  -   Function to view  Customers details
def customer_view():
    print("\n\n")
    print("\t\t\tCustomer History")
    print("="*75)
    print(" Cust_ID \t  Cust_Name  \t     DateTime  \t\t Amount   \t   Mobile ")
    print("="*75)
    cursor.execute("SELECT * FROM Customer")
    res = cursor.fetchall()
    for i in res:      
        print("   {}  \t  {} \t\t {} \t {}\t\t{} ".format(i[0],i[1],i[2],i[3],i[4]))
    print("="*75,"\n\n")





    
# Fifth Page  -  Function to change the login  credentials
def change_credentials():
    print("\n\n","-"*100)
    print("\t\t\tUpdating Profile")
    print("-"*100,"\n")
    b = 0
    while(True):
        print("\t\tOld  Details \n")
        name = input("\t\tUsername :: ")
        password = int(input("\t\tPassword :: "))
        print("\n")
        global UserName
        global Password 
        if (name == UserName and password == Password):
            b = 0
            print("\t\tNew Details \n")
            new_name = input("\t\tUsername    ::   ")
            new_pass = int(input("\t\tPassword    ::  "))
            
            UserName  = new_name        
            Password = new_pass
            print("\n\n","*"*70,"\n\n")
            break

        elif (b>4):
            print("\n\n","-"*100)
            print("\t\tYou Have Attempted Maximum Number of times")
            print("-"*100)
            print("\t\tYou have been redirected to Logging Page")
            print("-"*100,"\n\n")
            return
        
        else:       
            print("\n\n","-"*100)
            print("\t\tUser  Name or  Password  does  not  match")
            print("\t\t\tTry again")
            print("-"*100,"\n\n")
            b += 1



            

# Fourth page  -  Function To update Bakery Menu
def menu_update():
    print("\n\n","-"*100)
    print("\t\t\tUpdating Page")
    print("-"*100,"\n")
    while(True):
            print("\t\t Press 1 --    Add New Product")
            print("\t\t Press 2  --   Update Product Name")
            print("\t\t Press 3  --   Update Quantity")
            print("\t\t Press 4  --   Update Price")
            print("\t\t Press 5  --   Update Category")         
            print("\t\t Press 6  --   Return to Owner Page \n")
            choice = int(input("\t\t Your Choice  ::  \t"))

            if (choice == 1):
                print("\n\n","*"*70,"\n")
                prod_id = int(input(" Enter New Product ID  ::  "))
                prod_name = input(" Enter  Product  Name  ::  ")
                prod_quantity = int(input(" Enter Product  Quantity  :: "))
                prod_price = float(input(" Enter  Product  Price  ::  "))
                category = input(" Enter  Product  Category  ::  ")
                cursor.execute("INSERT INTO  Itemslist (product_id,product_name,product_quantity,product_price,category) VALUES (%s,%s,%s,%s,%s)",(prod_id,prod_name,prod_quantity,prod_price,category))
                
                connect.commit()
                print("\n","*"*70,"\n")
                
            elif (choice > 1 and choice <6):
                print("\n\n","*"*70,"\n")
                ID = int(input("   Enter  Product  Id  of  product  whose  details  you  want  to  update   ::  "))
                
                if(choice == 2):
                    x  = input("   New Product Name  ::  ")
                    cursor.execute("update itemslist set product_name=%s where product_id=%s",(x,ID))
                    
                elif(choice == 3):
                    x  = int(input("   New Quantity  ::  "))
                    cursor.execute("update itemslist set product_quantity=%s where product_id=%s",(x,ID))
                    
                elif(choice == 4):
                    x  =float(input("   New Product Price  ::  "))
                    cursor.execute("update itemslist set product_price=%s where product_id=%s",(x,ID))
                    
                elif(choice == 5):
                    x = input("  New  Category  ::  ")
                    cursor.execute("update itemslist set category=%s where product_id=%s",(x,ID))
                    
                connect.commit()
                print("\n","*"*70,"\n")
                    
            else:
                print("\n\n","*"*70,"\n\n")
                return



    

# Third page - Function To view the bakery menu
def menu_view_o():
    print("\n\n")
    print("\t\t\t\tBakery  Menu")
    print("="*70)
    print(" Prod_ID \t\t Product Name \t\t Quantity  \t Price ")
    print("="*70)
    cursor.execute("SELECT * FROM Itemslist")
    res = cursor.fetchall()
    for i in res:      
        print(" {} \t\t {} \t\t {} \t\t {} ".format(i[0],i[1],i[2],i[3]))
    print("="*70,"\n\n")





# Second page  -  Function to ask for choice of owner
def owner_page():
        print("\n\n","-"*100)
        print("\t\t\tLogged  In  Successfully")
        print("-"*100,"\n")
        while(True):
            print("\t\t Press 1  --   View Menu")
            print("\t\t Press 2  --   Update Menu")
            print("\t\t Press 3  --   Change Logging Credentials")
            print("\t\t Press 4  --   View Customer Details")
            print("\t\t Press 5  --   Return to Logging Page \n")
            choice = int(input("\t\t Your Choice  ::  \t"))

            if(choice == 1):
                menu_view_o()
            elif(choice == 2):
                menu_update()
            elif(choice == 3):
                change_credentials()
                return
            elif(choice == 4):
                customer_view()
            else:
                print("\n\n","*"*70,"\n\n")
                return





# First page  -  function to  check the  correct owner
def owner():
    print("\n\n","-"*100)
    print("\t\t\tWelcome  Sir / Mam")
    print("-"*100,"\n")

    b = 0
    while(True):
        print("\tEnter Your Logging Credentials")
        user_name = input("\tUser Name    :: \t")
        password = int(input("\tPassword       :: \t" ))

        if(user_name == UserName and password ==  Password ):
            owner_page()
            b = 0 

        else:
            b = b+1

            if(b<4):
                print("\n\n","-"*100)
                print("\t\tUser  Name or  Password  does  not  match")
                print("\t\t\tTry again")
                print("-"*100,"\n\n")

            else:
                print("\n\n","-"*100)
                print("\tYou have attempted the maximum number of  attempt")
                print("-"*100)
                print("\tYou have been redirected to Home page")
                print("-"*100,"\n\n")
                break

#                                                                                                                       CUSTOMER    PAGES
####################################################################################################################




# Eight Page - function to  enter information of customer in the database of bakery
def customer_detail(datetime,amount):
        global Name
        global Mobile
        cursor.execute("INSERT INTO Customer(Customer_name,Date_Time,Amount,Mobile)  VALUES (%s,%s,%s,%s)",(Name,datetime,amount,Mobile))
        connect.commit()




#  Seventh Page - function to display bill to the owner
def bill_display():
    global Name
    global Mobile
    print("\n\n","="*70)
    print("\t\t\t\tBILL ")
    print("="*70)

    now = datetime.datetime.utcnow()+datetime.timedelta(hours=5.5)
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H : %M : %S")
    DATETIME = now.strftime("%Y-%m-%d %H:%M:%S")

    print(" Customer Name ::  ",Name,"\t\t\t Date :: ",date)
    print(" Mobile  Number ::  ",Mobile,"\t\t Time :: ",time)
    print("="*70)    
    print("  S.no \t Product Name\t\tQuantity  \t Unit Price\t Price")
    print("="*70)
    cursor.execute("SELECT * FROM bill")
    res = cursor.fetchall()
    price = 0
    for i in res:      
        print("  {} \t {} \t\t  {} \t\t {} \t\t {} ".format(i[0],i[1],i[2],i[3],i[4]))
        price += i[4]
    GST = round(price*0.16,2)
    
    total = (price+GST)//1
    print("="*70)
    print("  Amount(Rs)        ::  ", price)
    print("  GST(16%)             ::  ",GST)
    print("  Total Amount     ::  ",total)
    print("="*70,"\n\n")
    cursor.execute("TRUNCATE TABLE bill")
    connect.commit()
    customer_detail(DATETIME,total)
    
  





# Sixth Page - function to enter buyed item by customer into bill.
def customer_prod_list(s,data,quantity):
        serial = s
        prod_name = data[1]
        prod_quantity = quantity
        prod_unit_price = data[3]
        price = prod_quantity * prod_unit_price

        cursor.execute("INSERT INTO Bill  VALUES (%s,%s,%s,%s,%s)",(serial,prod_name,prod_quantity,prod_unit_price,price))
        connect.commit()

        new_quantity = data[2] - quantity
        ID = data[0]

        cursor.execute("update itemslist set product_quantity=%s where product_id=%s",(new_quantity,ID))
        connect.commit()






# Fifth Page -  Function to ask customer about ordering
def product_order():
    print("\n\n","-"*100)
    print("\t\t\t ORDER PAGE ")
    print("-"*100,"\n\n")
    print("\t\t Press 1  --   To Buy Products ")
    print("\t\t Press 2  --   Return To Home Page")
    choice = int(input("\t\t Your Choice  ::  \t"))
    print("\n","-"*100)    

    if(choice == 1):
            
            c = 1
            while(True):                     
                print("\t\t Product Number   ::    ",c)
                ID =  int(input("\t\t Product ID          ::\t"))
                quantity =int(input("\t\t Quantity             ::\t"))

                if(ID>=1 and ID<=145):
                    cursor.execute("SELECT * FROM Itemslist WHERE product_id = %s",(ID,))
                    res =  cursor.fetchone()
                    print("-"*100)

                    print("\tYou Have Ordered  {}  and  quantity  {}".format(res[1],quantity))
                    print("\t\t Press 1  --   To Confirm Order")
                    print("\t\t Press 2  --   To Cancel Order")
                    choice = int(input("\t\t Your Choice  ::  "))
                    

                    if(choice == 1):
                        print("\t\t Order Successful ")
                        customer_prod_list(c,res,quantity)
                        c  = c+1
                        print("-"*100)

                    else:
                        print("\t\t Order Cancelled ")
                        print("-"*100)
                        continue

                else:
                    print("\n","-"*100)
                    print("\t Invalid Product ID! Please Try Again")
                    print("-"*100,"\n")
                    
                
                print("\n\n","-"*100)
                choice  =  int(input("\t Press 1  to buy another product Else Press 2   ::   "))
                print("-"*100,"\n\n")
                
                
                if(choice != 1):
                     bill_display()
                     return






# Fourth page -  Function to show menu to the customer
def menu_view_c_full():
    print("\n\n")
    print("\t\t\t\tBakery  Menu")
    print("="*70)
    print(" Prod_ID \t\t Product Name \t\t Quantity  \t Price ")
    print("="*70)
    cursor.execute("SELECT * FROM Itemslist WHERE product_quantity >= 5")
    res = cursor.fetchall()
    for i in res:      
        print(" {} \t\t {} \t\t {} \t\t {} ".format(i[0],i[1],i[2],i[3]))
    print("="*70,"\n\n")
    product_order()
    return



    


# Third Page -  function to show menu to the customer acordig to customer choice of particular product category.
def category():
    print("\n\n","-"*100)
    print("-"*100,"\n\n")
    
    print("\t\t Category Menu Available")
    print("\t\t Press 1  --   Bread  Menu ")
    print("\t\t Press 2  --   Pastries Menu")
    print("\t\t Press 3  --   Cookies Menu")
    print("\t\t Press 4  --   Pie Menu")
    print("\t\t Press 5  --   Return To Customer Page")

    choice = int(input("\t\t Your Choice  ::  \t"))

    if(choice >= 1 and choice <=4):
            print("\n\n")
            print("\t\t\t\tBakery  Menu")
            print("="*70)
            print(" Prod_ID \t\t Product Name \t\t Quantity  \t Price ")
            print("="*70)
            
            if(choice == 1):
                x = "Bread"
            elif(choice == 2):
                x = "Pastries"
            elif(choice == 3):
                x = "Cookies"
            elif(choice == 4):
                x = "Pie"
            cursor.execute("SELECT * FROM Itemslist WHERE category = %s  and product_quantity >= 5",(x,))
            res = cursor.fetchall()
            for i in res:      
                print(" {} \t\t {} \t\t {} \t\t {} ".format(i[0],i[1],i[2],i[3]))
            print("="*70,"\n\n")

            product_order()
            return
    
    else:
        print("\n\n","*"*70,"\n\n")
        return




    
# Second Page - Function To ask Customer his motive of viewing the bakery site.

def customer_page(name):
    print("\n\n","-"*100)
    print("\t\t\t WELCOME ",name.upper())
    print("-"*100,"\n\n")

    while(True):
            print("\t\t Press 1  --   View Full Menu")
            print("\t\t Press 2  --   View Menu Based On Your Choice")
            print("\t\t Press 3  --   Return to Home Page \n")
            choice = int(input("\t\t Your Choice  ::  \t"))

            if(choice == 1):
                menu_view_c_full()
                return 
            elif(choice == 2):
                category()
                return
            else:
                return
            


 

# First Page - Function to ask Customer His/Her Details

def customer():
    print("\n\n","-"*100)
    print("\t\t\t WELCOME ")
    print("-"*100,"\n\n")

    while(True):
        print("\t\t Kindly   Enter    Your    Details")
        name = input("\t\t Name  ::\t")
        mobile = int(input("\t\t Mobile Number ::\t"))

        if(name == "" or mobile > 9999999999  or mobile < 999999999):
            print("\n\n","-"*100)
            print("\t\tYour Name or Mobile Number is Not Entered  Properly")
            print("\t\t\tTry again")
            print("-"*100,"\n\n")

        else:
            global Name
            global Mobile
            Name = name
            Mobile = mobile
            customer_page(name)
            return


            

#                                                                                                          MAIN   PAGE  CODE  
####################################################################################################################


while(True):
    print("\n\n","-"*100)
    print("\t\t\tFun Food Bakery")
    print("-"*100,"\n")

    print("\t\t Press 1  --   If  you  are  Owner  \n\t\t Press 2  --   If  you  are  Customer \n\t\t Press 3  --   Exit from the site\n")
    choice = int(input("\t\t Your Choice  ::  \t"))

    if(choice == 1):
        owner()
    elif(choice == 2):
        customer()
    elif(choice == 3):
        print("\n\n","-"*100)
        print("\t\t\tHave  A  Good  Day ")
        print("-"*100,"\n")
        break
    else:
        print(" Please Enter Correct Choice ")
    

#####################################################################################################################

