        

import json
import datetime
from All_path.path import Menu_path
# from Domain.Table.table_booking import booked_table

# from Domain.bill_manage.bill import order_item_generate_bill

        
class Menu_Details:
    # Load menu from JSON file
    def load_menu_details(self,path):
        self.path=path
        with open(self.path, 'r') as file:
            self.load_menu = json.load(file)

    # Display the loaded menu
    def display_menu_details(self):
        try:
            print()
            print('*******Breakfast menu details*****')
            print()
            # Show Breakfast menu
            print(json.dumps(self.load_menu[0], indent=4))  
            print()
            print('*******Lunch Menu details****')
            print()
            # Show Lunch menu
            print(json.dumps(self.load_menu[1], indent=4))  
        except Exception as e:
            date = datetime.datetime.now()
            error_list = {'error': str(e), 'function_name': 'display_menu_details', 'class': 'Restaurant', 'date': date}
            print('Technical issue please wait!')

# Main function to display menu or book table
def menu_details():
    while True:
        print()
        print('=' * 20)
        print('1. Check menu details...')
        
        print('2. Exit...')
        print('=' * 20)
        print()

        so_menu = input('Enter any option: ')
        if so_menu.isdigit():
            so_menu = int(so_menu)
            if so_menu == 1:
                data=Menu_Details()
                data.load_menu_details(Menu_path)
                data.display_menu_details()
                
                # call the function ordering item and generate bill
                # order_item_generate_bill() 
                break
            elif so_menu == 2:
            
                break
            
            else:
                print('Select correct option (1/2/3)')
        else:
            print('Enter only digit number!')
