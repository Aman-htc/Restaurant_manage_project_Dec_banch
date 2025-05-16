
# # Importing json for reading and writing JSON data
import json
import datetime

from Error_handal.logger import write_logs
from All_path.path import  Load_amount_path, Save_order_path, Staff_path,table_booked_details


# # Parent class
class Check_Staff:
    try:
        

        def admin_data(self, path):
            self.path = path
            with open(self.path, 'r') as file:
                # Load JSON data into self.data_store
                self.data_store = json.load(file)  

        

        # Method to display all loaded data in formatted JSON
        def all_display_store_data(self):
            print(json.dumps(self.data_store, indent=4))
    except Exception as e:
        error_list={'error':str(e),'class_name':'Check_staff'}
        write_logs(str(error_list))
        print('Technical issue please wait!')

# # Subclass for handling order
class Order_List:
    try:
        
        def __init__(self,path):
            self.order_path = path
            with open(self.order_path, 'r') as file:
                self.data_store = json.load(file)  # Load order data
            
        def load_order(self):
            
            # Ask user how many past days of orders to display
            self.num_days = int(input("Enter the number of past days to views order details?: "))

            self.today = datetime.datetime.now().date()  # Current date
            self.start_date = self.today - datetime.timedelta(days=self.num_days)  # Start date

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
                    print(json.dumps(order,indent=4))
                    found = True

            if not found:
                print("No orders found in this date range.")
                
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
        
            
def order_data():
    print('-'*30)
    print('1. Order details check!!')            
    print('2. Confirm order details!')
    print('3. Cancel order details!')
    print('4. Exit!')
    print('-'*30)
    while True:
        
        input_data=input('Select any option: ')
        if input_data.isdigit():
            input_data=int(input_data)
            if input_data == 1:
                data=Order_List(Save_order_path)
                
                data.load_order()
                
            elif input_data == 2:
                data=Order_List(Save_order_path)    
                
                data.confirm()
            elif input_data == 3:
                data= Order_List(Save_order_path)    
        
                data.cancel()
            elif input_data == 4:
                break    
        else:
            print('enter your digit number!')
            


 
class Amount_list():
    try:
        
        def __init__(self, path):
            self.amount_path = path
            with open(self.amount_path, 'r') as file:
                self.data_store = json.load(file)  # Load amount data
        

        def load_amount(self):
            

            # Ask user how many past days of orders to display
            self.num_days = int(input("Enter the number of past days to views bills details: "))

            self.today = datetime.datetime.now().date()  # Current date
            self.start_date = self.today - datetime.timedelta(days=self.num_days)  # Start date

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
                    print(json.dumps(order,indent=4))
                    found = True

            if not found:
                print("No orders found in this date range.")

        def online_check(self):
            for n in self.data_store:
                for key,value in n.items():
                    if key ==  'payment' and value == 'online':
                        print(n)
                    
        def cash_check(self):
            for n in self.data_store:
                for key,value in n.items():
                    if key == 'payment' and value == 'cash':
                        print(n)                       
    except Exception as e:
        error_list={'error':str(e),'class_name':'Amount_list'}
        write_logs(str(error_list))
        print('Technical issue please wait!')
        
def amount_check():
    
    print('-'*30)
    print('1. check amount details!')
    print('2. Check online payment!')
    print('3. Check cash payment!')
    print('4. Exit!')
    print('-'*30)
    while True:
        
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
    
                
# Check book table funcation 
def table_details(path):
    table_path = path  # Make sure 'path' variable is set to your JSON file path

    with open(table_path, 'r') as file:
        table_load = json.load(file)

    num_days = int(input("Enter the number of past days to view table details: "))

    today = datetime.datetime.now().date()
    start_date = today - datetime.timedelta(days=num_days)

    found = False

    for order in table_load:
        order_time_str = order.get("datetime", "")
        try:
            order_datetime = datetime.datetime.strptime(order_time_str, "%Y-%m-%d %H:%M:%S")
        except Exception:
            continue

        order_date = order_datetime.date()

        if start_date <= order_date <= today:
            print(json.dumps(order, indent=4))
            found = True

    if not found:
        print("No bookings found in the given date range.")

                     



# Main function to check various data types
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
        
