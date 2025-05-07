        

import json
import datetime
from All_path.path import Menu_path
# from Domain.Table.table_booking import booked_table

# from Domain.bill_manage.bill import order_item_generate_bill

# Class to handle restaurant menu-related operations
class Restaurant:
    def __init__(self, path):
        self.path = path 

    # Save the current menu list to a JSON file
    def save_menu_details(self):
        with open(self.path, 'w') as file:
            json.dump(self.menu_list, file, indent=4)

    # Define the menu items for breakfast and lunch
    def menu_details(self):
        try:
            self.menu_list = []
            print('---------Restaurant Menu-------------')

            # Define Breakfast menu
            self.Breakfast_menu = [
                {'id': 1, 'type': 'full', 'name': 'aloo paratha-f', 'price': 50},
                {'id': 2, 'type': 'haph', 'name': 'allo paratha-h', 'price': 30},
                {'id': 3, 'type': 'full', 'name': 'chana ghugni-f', 'price': 40},
                {'id': 4, 'type': 'haph', 'name': 'chana ghugani-h', 'price': 20},
                {'id': 5, 'type': 'full', 'name': 'sattu paratha-f', 'price': 50},
                {'id': 6, 'type': 'haph', 'name': 'sattu paratha-h', 'price': 30},
                {'id': 7, 'type': '100g', 'name': 'jalebi-g', 'price': 40},
                {'id': 8, 'type': 'haph', 'name': 'chai-h', 'price': 20},
                {'id': 9, 'type': 'full', 'name': 'salad-f', 'price': 40},
                {'id': 10, 'type': 'haph', 'name': 'salad-h', 'price': 20}
            ]

            # Define Lunch menu
            self.Lunch_menu = [
                {'id': 1, 'type': 'full', 'name': 'litte chokha-f', 'price': 60},
                {'id': 2, 'type': 'haph', 'name': 'litte chokha-h', 'price': 30},
                {'id': 3, 'type': 'full', 'name': 'rice dal-f', 'price': 70},
                {'id': 4, 'type': 'haph', 'name': 'rice dal-h', 'price': 40},
                {'id': 5, 'type': 'full', 'name': 'paneer butter masala-f', 'price': 200},
                {'id': 6, 'type': 'haph', 'name': 'paneer butter masala-h', 'price': 110},
                {'id': 7, 'type': 'full', 'name': 'shahi paneer-f', 'price': 180},
                {'id': 8, 'type': 'haph', 'name': 'shahi paneer-h', 'price': 100},
                {'id': 9, 'type': 'full', 'name': 'plain rice-f', 'price': 50},
                {'id': 10, 'type': 'haph', 'name': 'roti-h', 'price': 50},
                {'id': 11, 'type': 'full', 'name': 'kadhi chawal-f', 'price': 120},
                {'id': 12, 'type': 'haph', 'name': 'kadhi chawal-h', 'price': 70}
            ]

            # Append both menus to the main list
            self.menu_list.append(self.Breakfast_menu)
            self.menu_list.append(self.Lunch_menu)

        except Exception as e:
            date = datetime.datetime.now()
            error_list = {'error': str(e), 'function_name': 'menu_details', 'class': 'Restaurant', 'date': date}
            print('Technical issue please wait!')

    # Load menu from JSON file
    def load_menu_details(self):
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
                # Create Restaurant object and perform full menu details
                data = Restaurant(Menu_path)
                data.menu_details()
                data.save_menu_details()
                data.load_menu_details()
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
