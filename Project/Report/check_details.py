import json
from All_path.path import Menu_path , Load_amount_path, Save_order_path,Staff_path,table_path
class Check_Admin:
    def admin_data(self,path):
        self.path=path
        with open(self.path,'r') as file:
            self.data_store=json.load(file)
        
    def input_data(self):
        self.enter_name=input('please enter your data: ')
        found=False
        for item in self.data_store:
            for key,value in item.items():
                if value == self.enter_name:
                    print(item)
                    found=True
        if not found:
            print('invalid name no  store this data')            
    def all_display_store_data(self):
        print(json.dumps(self.data_store,indent=4))        

class Order_List(Check_Admin):
    def load_order(self,path):
        self.order_path=path
        with open(self.order_path,'r') as file:
            self.data_store=json.load(file)
                
                
class Amount_list(Check_Admin):
    def load_amount(self,path):
        self.amount_path=path
        with open(self.amount_path,'r') as file:
            self.data_store=json.load(file)

class Table_book(Check_Admin):
    def load_table(self,path):
        self.table_path=path
        with open(self.table_path,'r') as file:
            self.data_store=json.load(file)

              

        

def all_data_check():
    print('='*30)
    print()                        
    print('1. Amount details check..')
    print('2. 0rder item check..')
    print('3. Staff details check...')
    print('4. Table details check...')
    print()
    print('='*30)
    
    while True:
        
        select=int(input('Select any option: '))
        if select == 1:
            data=Amount_list()
            data.load_amount(Load_amount_path)
            data. input_data()
            data.all_display_store_data()
        elif select == 2:
            data=Order_List()
            data.load_order(Save_order_path)
            data. input_data()
            data.all_display_store_data()
        
        elif select == 3:
            data=Check_Admin()
            data.admin_data(Staff_path)
            data.input_data()
            data.all_display_store_data()
        elif select ==4:
            data= Table_book()  
            data.load_table(table_path)
            data.all_display_store_data()
        elif select == 5:
            break    
        else:
            print('enter your digit number or not invalid number!')        
            
                
# Importing json for reading and writing JSON data
import json


from All_path.path import Menu_path, Load_amount_path, Save_order_path, Staff_path, table_path

# Parent class
class Check_Admin:

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
class Order_List(Check_Admin):
    def load_order(self, path):
        self.order_path = path
        with open(self.order_path, 'r') as file:
            self.data_store = json.load(file)  # Load order data


# Subclass for handling amount list, inherits from Check_Admin
class Amount_list(Check_Admin):
    def load_amount(self, path):
        self.amount_path = path
        with open(self.amount_path, 'r') as file:
            self.data_store = json.load(file)  # Load amount data


# Subclass for handling table booking details, inherits from Check_Admin
class Table_book(Check_Admin):
    def load_table(self, path):
        self.table_path = path
        with open(self.table_path, 'r') as file:
            self.data_store = json.load(file)  # Load table data


# Main function to check various data types
def all_data_check():
    print('='*30)
    print()
    print('1. Amount details check..')
    print('2. Order item check..')
    print('3. Staff details check...')
    print('4. Table details check...')
    print()
    print('='*30)

    while True:
        # Prompting user to select an option
        select = int(input('Select any option: '))

        # Option 1: Load and display amount data
        if select == 1:
            data = Amount_list()
            data.load_amount(Load_amount_path)
            # data.input_data()
            data.all_display_store_data()

        # Option 2: Load and display order data
        elif select == 2:
            data = Order_List()
            data.load_order(Save_order_path)
            # data.input_data()
            data.all_display_store_data()

        # Option 3: Load and display staff data
        elif select == 3:
            data = Check_Admin()
            data.admin_data(Staff_path)
            # data.input_data()
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
       
    
                    