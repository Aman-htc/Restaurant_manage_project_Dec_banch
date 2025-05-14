
# Importing json for reading and writing JSON data
import json


from All_path.path import Menu_path, Load_amount_path, Save_order_path, Staff_path, table_path

# Parent class
class Check_Staff:

    def admin_data(self, path):
        self.path = path
        with open(self.path, 'r') as file:
            # Load JSON data into self.data_store
            self.data_store = json.load(file)  

    # Method to prompt user input and check if it matches any entry in the loaded data
    def input_data(self):
        self.enter_name = input('please enter your data: ')
        found = False
        for item in self.data_store:
            for key, value in item.items():
                if value == self.enter_name:
                    # Print the matching record
                    print(item)  
                    found = True
        if not found:
            print('invalid name no store this data')  # If no match found

    # Method to display all loaded data in formatted JSON
    def all_display_store_data(self):
        print(json.dumps(self.data_store, indent=4))


# Subclass for handling order list, inherits from Check_Admin
class Order_List(Check_Staff):
    def load_order(self, path):
        self.order_path = path
        with open(self.order_path, 'r') as file:
            self.data_store = json.load(file)  # Load order data
            
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
            
def order_data():
    print('-'*30)
    print('1. All data check!')            
    print('2. Confirm order details!')
    print('3. Cancel order details!')
    print('4. Exit!')
    print('-'*30)
    while True:
        
        input_data=input('Select any option: ')
        if input_data.isdigit():
            input_data=int(input_data)
            if input_data == 1:
                data=Order_List()
                data.load_order(Save_order_path)
                data. all_display_store_data()
            elif input_data == 2:
                data=Order_List()    
                data.load_order(Save_order_path)
                data.confirm()
            elif input_data == 3:
                data= Order_List()    
                data.load_order(Save_order_path)
                data.cancel()
            elif input_data == 4:
                break    
        else:
            print('enter your digit number!')
            


# Subclass for handling amount list, inherits from Check_Admin
class Amount_list(Check_Staff):
    def load_amount(self, path):
        self.amount_path = path
        with open(self.amount_path, 'r') as file:
            self.data_store = json.load(file)  # Load amount data
            
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

        
def amount_check():
    
    print('-'*30)
    print('1. check all amount details!')
    print('2. Check online payment!')
    print('3. Check cash payment!')
    print('4. Exit!')
    print('-'*30)
    while True:
        
        input_data=input('Select any option: ')
        if input_data.isdigit():
            input_data=int(input_data)
            if input_data == 1:
                data=Amount_list()
                data.load_amount(Load_amount_path)
                data.all_display_store_data()
            elif input_data == 2:
                data=Amount_list()    
                data.load_amount(Load_amount_path)
                data.online_check()
            elif input_data == 3:
                data=Amount_list()
                data.load_amount(Load_amount_path)
                data.cash_check()
            elif input_data == 4:
                break    
        else:
            print('enter your only digit number(1/2/3)')
    
                
    
            


# Subclass for handling table booking details, inherits from Check_Admin
class Table_book(Check_Staff):
    def load_table(self, path):
        self.table_path = path
        with open(self.table_path, 'r') as file:
            self.data_store = json.load(file)  # Load table data


# Main function to check various data types
def all_data_check():
    while True:
        print('='*30)
        print()
        print('1. Amount details check..')
        print('2. Order item check..')
        print('3. Staff details check...')
        print('4. Table details check...')
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

        # Option 4: Load and display table data
        elif select == 4:
            data = Table_book()
            data.load_table(table_path)
            data.all_display_store_data()

        # Option 5: Exit the loop
        elif select == 5:
            break

        # Invalid input case
        else:
            print('enter your digit number or not invalid number!')
       
    
                    