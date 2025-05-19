        

import json
import datetime
from All_path.path import Menu_path
from Error_handal.logger import write_logs


from Domain.Table.table_booking import table_cancel_booked
from Report.check_details import order_data

        
class Menu_Details:
    # Load menu from JSON file
    def load_menu_details(self,path):
        self.path=path
        with open(self.path, 'r') as file:
            self.load_menu = json.load(file)

    # Display the loaded menu
    def display_menu_details(self):
        try:
            print('*'*60)
            print('*'+' RESTAURANT MENU DETAILS'.center(58)+'*')
            print('*'*60)
            print()
            print('*'*60)
            print('*'+'BREAKFAST MENU DETAILS'.center(58)+'*')
            print('*'*60)
            print()
            # Show Breakfast menu
            
            print('*'*60)
            print()
            print(f'{'ID':<10} {'Item Name':<24} {'Type':<15} {'Price':<10}')
            print()
            print('-'*60)
            for n in self.load_menu[0]:
                print(f"{n['id']:<10} {n['name']:<24} {n['type']:<15} {n['price']:<10} ")
                print()
                print('-'*60)
            print('='*60)    
            print()            
            print('*'*60)
            print('*'+'LUNCH MENU DETAILS'.center(58)+'*')
            print('*'*60)
            # Show Lunch menu
            print()
            print('='*60)
            print()
            print(f'{'ID':<10} {'Item Name':<24} {'Type':<15} {'Price':<10}')
            print()
            print('-'*60)
            for n in self.load_menu[1]:
                print(f"{n['id']:<10} {n['name']:<24} {n['type']:<15} {n['price']:<10} ")
                print()
                print('-'*60)
            print('='*60)    
        except Exception as e:
            date = datetime.datetime.now()
            error_list = {'error': str(e), 'function_name': 'display_menu_details', 'class': 'Menu_Deatails', 'date': date}
            write_logs(str(error_list))
            print('Technical issue please wait!')
def check_menu():
    data=Menu_Details()
    data.load_menu_details(Menu_path)
    data.display_menu_details()
                

# Main function to display menu or book table
def menu_details():
    while True:
        print()
        print('=' * 20)
        print('1. Check menu details...')
        print('2. Check Order details..')
    
        print('3. Exit...')
        print('=' * 20)
        print()

        so_menu = input('Enter any option: ')
        if so_menu.isdigit():
            so_menu = int(so_menu)
            if so_menu == 1:
                check_menu()
                # data=Menu_Details()
                # data.load_menu_details(Menu_path)
                # data.display_menu_details()
                
                # table_cancel_booked()
                table_cancel_booked()
                
                
            
                
            elif so_menu == 2:
                order_data()
            elif so_menu == 3:
                break    
            
            else:
                print('Select correct option (1/2/3)')
        else:
            print('Enter only digit number!')
