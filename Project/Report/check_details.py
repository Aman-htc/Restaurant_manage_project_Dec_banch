
# # Importing json for reading and writing JSON data
import json
import datetime

from Error_handal.logger import write_logs
from All_path.path import  Load_amount_path, Save_order_path, Staff_path,table_booked_details


# # Parent class
# -------------------------------ALL STAFF CHECK CLASS Check_Staff----------------------------
class Check_Staff:
    try:
        

        def admin_data(self, path):
            self.path = path
            with open(self.path, 'r') as file:
                # Load JSON data into self.data_store
                self.data_store = json.load(file)  

        

        # Method to display all loaded data in formatted JSON
        def all_display_store_data(self):
            print(f"{'Staff_Id':<15} {'Staff_name':<10} {'Staff_email':<15} {'Contact':<15} {'Password':<15} ")
            print('*'*100)
            
            for data in self.data_store:
                for key,value in data.items():
                    if value == 'staff':
                        
                        print(f"{data['id']:<15} {data['name']:<10} {data['email']:<15} {data['contact']:<15}  {data['password']:<15} ")
                        print('-'*100)
    except Exception as e:
        error_list={'error':str(e),'class_name':'Check_staff'}
        write_logs(str(error_list))
        print('Technical issue please wait!')
        

# ----------------------------------------Order details check report class Order_list --------------------------
class Order_List:
    try:
        
        def __init__(self,path):
            self.order_path = path
            with open(self.order_path, 'r') as file:
                self.data_store = json.load(file)  # Load order data
            
        def load_order(self):
            while True:
                print()
                print('='*30)
                
                print('1. Today Check Order..')
                print('2  One Week Check Order..')
                print('3. One Month Check Order..')
                print('4. Exit..')
                print('='*30)
                
                self.order_check=input('Enter your select option: ')
                if self.order_check.isdigit():
                    self.order_check = int(self.order_check)
                    if self.order_check == 1:
                        

                        self.today = datetime.datetime.now().date()  # Current date
                        self.start_date = self.today - datetime.timedelta(days=0)  # Start date

                        print(f"{'User_name':<10} {'Item_ID':<7} {'Item_name':<10} {'Quantity':<15} {'datetime':<27} {'Order':<15} {'Price'}")
                        print('*'*100)
                        found = False
                        for order in self.data_store:
                            order_time_str = order.get("datetime", "")
                            try:
                                # Convert datetime string to date
                                order_date = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S.%f").date()
                            except Exception as e:
                                continue  # Skip if format is invalid

                            # Check if order date is within the range
                            if self.start_date <= order_date <= self.today:
                                print(f" {order["user_name"]:<11} {order['item_id']:<5} "
                                    f"{order['Item_name']:<13} {order['Quantity']:<5} {order['datetime']:<28} {order['Order']:<16}{order["price"]}")
                                print('-'*100)
                                found = True

                        if not found:
                            print("No orders found in this date range.")
                            
                    elif self.order_check == 2:
                        
                        self.today = datetime.datetime.now().date()  # Current date
                        self.start_date = self.today - datetime.timedelta(days=7)  # Start date

                        print(f"{'User_name':<10} {'Item_ID':<7} {'Item_name':<10} {'Quantity':<15} {'datetime':<27} {'Order':<15} {'Price'}")
                        print('*'*100)
                        found = False
                        for order in self.data_store:
                            order_time_str = order.get("datetime", "")
                            try:
                                # Convert datetime string to date
                                order_date = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S.%f").date()
                            except Exception as e:
                                continue  # Skip if format is invalid

                            # Check if order date is within the range
                            if self.start_date <= order_date <= self.today:
                                # 
                                print(f" {order["user_name"]:<11} {order['item_id']:<5} "
                                    f"{order['Item_name']:<13} {order['Quantity']:<5} {order['datetime']:<28} {order['Order']:<16}{order["price"]}")
                                print('-'*100)
                                found = True
                        if not found:
                            
                            print("No orders found in this date range.")
                            
                    elif self.order_check == 3:
                        self.today = datetime.datetime.now().date()
                        self.start_date = self.today - datetime.timedelta(days=30)
                        
                        print(f"{'User_name':<10} {'Item_ID':<7} {'Item_name':<10} {'Quantity':<15} {'datetime':<27} {'Order':<15} {'Price'}")
                        print('*'*100)
                        found = False
                        
                        for order in self.data_store:
                            order_time_str = order.get("datetime", "")
                            try:
                                order_date = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S.%f").date()
                            except Exception as e:
                                continue

                            if self.start_date <= order_date <= self.today:
                                # Print the order
                                print(f" {order["user_name"]:<11} {order['item_id']:<5} "
                                    f"{order['Item_name']:<13} {order['Quantity']:<5} {order['datetime']:<28} {order['Order']:<16}{order["price"]}")
                                print('-'*100)
                                found = True

                        if not found:
                            print("No orders found in this date range.")

                    elif self.order_check == 4:
                        break        
                    else:
                        print('Enter your only (1/2/3/4)')            
                else:
                    print('Enter your digit number!')                
                
        def confirm(self):
            for n in self.data_store:
                for key,value in n.items():
                    if key == "Order" and value == "confirm":
                        print(n)
                        
        def cancel(self):
            for n in self.data_store:
                for key,value in n.items():
                    if key == "Order" and value == "cancel":
                        print(n)  
                                  
    except Exception as e:
        error_list={'error':str(e),'class_name':'Order_list'}
        write_logs(str(error_list))
        print('Technical issue please wait!')    
        
# ____________________________Order details check funcation call_________________________________
def order_data():
    while True:
        print('-'*30)
        print('1. Order details check!!')            
        # print('2. Confirm order details!')
        # print('3. Cancel order details!')
        print('2. Exit!')
        print('-'*30)
        
        
        input_data=input('Select any option: ')
        if input_data.isdigit():
            input_data=int(input_data)
            if input_data == 1:
                data=Order_List(Save_order_path)
                
                data.load_order()
                
            elif input_data == 2:
                break
            
        else:
            print('enter your digit number!')
            


# ----------------------------------Amount check report class Amount_list------------------------------------ 
class Amount_list():
    try:
        
        def __init__(self, path):
            self.amount_path = path
            with open(self.amount_path, 'r') as file:
                self.data_store = json.load(file)  # Load amount data
        

        def load_amount(self):
            
            

            while True:
                print()
                print('='*30)
                
                print('1. Today Check Bills..')
                print('2  One Week Check Bills..')
                print('3. One  Month Check Bills..')
                print('4. Exit..')
                print('='*30)
                
                self.order_check=input('Enter your select option: ')
                if self.order_check.isdigit():
                    self.order_check = int(self.order_check)
                    if self.order_check == 1:
                       

                        self.today = datetime.datetime.now().date()  # Current date
                        self.start_date = self.today - datetime.timedelta(days=0)  # Start date

                        print(f"{'User_name':<10} {'Gst Amount':<12} {'Total Amount':<15}  {'Datetime':<27} {'Payment':<15}")
                        print('*'*100)
                        found = False
                        for order in self.data_store:
                            order_time_str = order.get("datetime", "")
                            try:
                                # Convert datetime string to date
                                order_date = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S.%f").date()
                            except Exception as e:
                                continue  # Skip if format is invalid

                            # Check if order date is within the range
                            if self.start_date <= order_date <= self.today:
                                print(f" {order["Customer_name"]:<11} {order['gst amount']:<10} "
                                    f"{order['Total amount']:<13} {order['datetime']:<32} {order['payment']}")
                                print('-'*100)
                                found = True

                        if not found:
                            print("No orders found in this date range.")
                            
                    elif self.order_check == 2:
                        
                        self.today = datetime.datetime.now().date()  # Current date
                        self.start_date = self.today - datetime.timedelta(days=7)  # Start date

                        print(f"{'User_name':<10} {'Gst Amount':<12} {'Total Amount':<15}  {'Datetime':<27} {'Payment':<15}")
                        print('*'*100)
                        found = False
                        for order in self.data_store:
                            order_time_str = order.get("datetime", "")
                            try:
                                # Convert datetime string to date
                                order_date = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S.%f").date()
                            except Exception as e:
                                continue  # Skip if format is invalid

                            # Check if order date is within the range
                            if self.start_date <= order_date <= self.today:
                                # 
                                print(f" {order["Customer_name"]:<11} {order['gst amount']:<10} "
                                    f"{order['Total amount']:<13} {order['datetime']:<32} {order['payment']}")
                                print('-'*100)
                                found = True
                        if not found:
                            
                            print("No orders found in this date range.")
                            
                    elif self.order_check == 3:
                        self.today = datetime.datetime.now().date()
                        self.start_date = self.today - datetime.timedelta(days=30)
                        
                        print(f"{'User_name':<10} {'Gst Amount':<12} {'Total Amount':<15}  {'Datetime':<27} {'Payment':<15}")
                        print('*'*100)
                        found = False
                        
                        for order in self.data_store:
                            order_time_str = order.get("datetime", "")
                            try:
                                order_date = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S.%f").date()
                            except Exception as e:
                                continue

                            if self.start_date <= order_date <= self.today:
                                # Print the order
                                print(f" {order["Customer_name"]:<11} {order['gst amount']:<10} "
                                    f"{order['Total amount']:<13}  {order['datetime']:<32} {order['payment']}")
                                print('-'*100)
                                found = True
                        if not found:
                            print("No orders found in this date range.")

                    elif self.order_check == 4:
                        break        
                    else:
                        print('Enter your only (1/2/3/4)')            
                else:
                    print('Enter your digit number!')
        def online_check(self):
            print(f"{'User_name':<10} {'Gst Amount':<12} {'Total Amount':<15} {'UPI':<15} {'Datetime':<27} {'Payment':<15}")
            print('*'*100)
            for n in self.data_store:
                for key,value in n.items():
                    if key ==  'payment' and value == 'online':
                        print(f" {n["Customer_name"]:<11} {n['gst amount']:<10} "
                            f"{n['Total amount']:<13} {n['upi']:<8} {n['datetime']:<32} {n['payment']}")
                        print('-'*100)
                    
        def cash_check(self):
            print(f"{'User_name':<10} {'Gst Amount':<12} {'Total Amount':<15}  {'Datetime':<27} {'Payment':<15}")
            for n in self.data_store:
                for key,value in n.items():
                    if key == 'payment' and value == 'cash':
                        print(f" {n["Customer_name"]:<11} {n['gst amount']:<10} "
                            f"{n['Total amount']:<13}  {n['datetime']:<32} {n['payment']}")
                        print('-'*100)                       
    except Exception as e:
        print(e)
        error_list={'error':str(e),'class_name':'Amount_list'}
        write_logs(str(error_list))
        print('Technical issue please wait!')
        
#__________________________amount details bill funcation call ________________________________________ 
def amount_check():
    while True:
        
    
        print('-'*30)
        print('1. check amount details!')
        print('2. Check online payment!')
        print('3. Check cash payment!')
        print('4. Exit!')
        print('-'*30)
    
        input_data=input('Select any option: ')
        if input_data.isdigit():
            input_data=int(input_data)
            if input_data == 1:
                data=Amount_list(Load_amount_path)
                data.load_amount()
                
            elif input_data == 2:
                data=Amount_list(Load_amount_path)    
            
                data.online_check()
            elif input_data == 3:
                data=Amount_list(Load_amount_path)
        
                data.cash_check()
            elif input_data == 4:
                break    
        else:
            print('enter your only digit number(1/2/3)')
    
                
#--------------------------------- Check book table  details funcation -----------------------------------------
import json
import datetime

def table_details(path):
    with open(path, 'r') as file:
        data_store = json.load(file)
    
    while True:
        print()
        print('='*30)
        print('1. Today Book Table Check..')
        print('2. One Week Book Table Check')
        print('3. One Month Book Table Check..')
        print('4. Exit..')
        print('='*30)

        order_check = input('Enter your select option: ')
        if order_check.isdigit():
            order_check = int(order_check)
            
            today = datetime.datetime.now().date()
            
            if order_check == 1:
                start_date = today
            elif order_check == 2:
                start_date = today - datetime.timedelta(days=7)
            elif order_check == 3:
                start_date = today - datetime.timedelta(days=30)
            elif order_check == 4:
                break
            else:
                print('Enter only (1/2/3/4)')
                continue

            print(f"{'User_name':<10} {'Book Seat':<12} {'Table No':<15} {'DateTime'} ")
            print('*'*100)
            found = False

            for order in data_store:
                order_time_str = order.get("datetime", "")
                try:
                    order_datetime = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S")
                except Exception:
                    continue

                if start_date <= order_datetime.date() <= today:
                    print(f" {order['name']:<11} {order['book_seat']:<10} "
                          f"{order['table_no']:<13} {order['datetime']}")
                    print('-'*100)
                    found = True

            if not found:
                print("No orders found in this date range.")
        else:
            print('Enter a valid digit (1/2/3/4)!')




# Main function to check various data types
# -----------------------------All class call main funcation all_data_check_--------------------------
def all_data_check():
    try:
        
        while True:
            print('='*30)
            print()
            print('1. Amount details check..')
            print('2. Order item check..')
            print('3. Staff details check...')
            print('4. Check book table!')
            print('5. Exit...')
            print()
            print('='*30)

        
            # Prompting user to select an option
            select = int(input('Select any option: '))

            # Option 1: Load and display amount data
            if select == 1:
                amount_check()
                
            
            # Option 2: Load and display order data
            elif select == 2:
                
                order_data()
                
            # Option 3: Load and display staff data
            elif select == 3:
                data = Check_Staff()
                data.admin_data(Staff_path)
                
                data.all_display_store_data()
                
            # Option 5: Exit the loop
            elif select == 4:
                table_details(table_booked_details)
            elif select == 5:
                break    

            # Invalid input case
            else:
                print('enter your digit number or not invalid number!')
    except Exception as e:
        error_list={'error':str(e),"funcation name":'all data check'}     
        write_logs(str(error_list))
        print('Technical issue please wait')
        
