    
    
    
import json
import datetime
from All_path.path import Menu_path
from Report.check_details import all_data_check_menu
from Error_handal.logger import write_logs

# Class to manage restaurant menu (add/remove items from Breakfast or Lunch menus)
class Manage_Restaurant:
    def __init__(self, path):
        self.path = path 
        
        # Load menu data from file
        with open(self.path, 'r') as file:
            self.menu_details = json.load(file)

    # function for managing menu items
    def manage_item(self):
        try:
            while True:
                print()
                print('*****Restaurant item manage*****')
                print('=' * 30)
                print('1. Add item to breakfast menu')
                print('2. Add item to lunch menu')
                print('3. Remove item from breakfast menu')
                print('4. Remove item from lunch menu')
                print('5. Exit')
                print('=' * 30)

                staff = input('Select any option: ')
                if staff.isdigit():
                    staff = int(staff)

                    # Add item to breakfast menu
                    if staff == 1:
                        self.item_list = {}
                        self.item_Id = int(input('Enter your item id: '))
                        self.item_name = input('Enter your item name: ')
                        self.item_price = int(input('Enter your item price: '))
                        self.item_category = input('Enter your type (haph ya full): ')
                        self.item_list['id'] = self.item_Id
                        self.item_list['item'] = self.item_name
                        self.item_list['price'] = self.item_price
                        self.item_list['type'] = self.item_category
                        # Add to breakfast menu
                        self.menu_details[0].append(self.item_list)  

                        # Save updated menu to file
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)

                    # Add item to lunch menu
                    elif staff == 2:
                        self.item_list = {}
                        self.item_Id = int(input('Enter your item id: '))
                        self.item_name = input('Enter your item name: ')
                        self.item_price = int(input('Enter your item price: '))
                        self.item_category = input('Enter your type (haph ya full): ')
                        self.item_list['id'] = self.item_Id
                        self.item_list['item'] = self.item_name
                        self.item_list['price'] = self.item_price
                        self.item_list['type'] = self.item_category  
                    
                        self.menu_details[1].append(self.item_list) 

                        # Save updated menu to file
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)

                    # Remove item from breakfast menu by index
                    elif staff == 3:
                        index_number = int(input('Enter item index number to remove: '))
                        self.menu_details[0].pop(index_number)

                        # Save only breakfast menu to file
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)  

                    # Remove item from lunch menu by index
                    elif staff == 4:
                        index_number = int(input('Enter item index number to remove: '))
                        self.menu_details[1].pop(index_number)

                        # Save full menu again
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)

                    elif staff == 5:
                        break  # Exit loop
                else:
                    print('Please enter a valid digit number.')

        except Exception as e:
            date = datetime.datetime.now()
            error_data = {
                'error': str(e),
                'funcation name': 'manage_item',
                'class': 'Manage_Restaurant',
                'date': date
            }
            write_logs(str(error_data))  # Log error
            print('Technical issue please wait!')

# Function to initialize the menu manager and open item manager
def item_manage():
    data = Manage_Restaurant(Menu_path)
    data.manage_item()

# Function to manage restaurant system: either update menu or view reports
def manage_and_report():
    while True:
        print()
        print('=' * 20)
        print('1. Manage item...')
        print('2. Check report...')
        print('3. Exit...')
        print('=' * 20)
        
        try:
            input_number = int(input('Select any option: '))
            if input_number == 1:
                # Open item manager
                item_manage()  
            elif input_number == 2:
                all_data_check_menu()  
            elif input_number == 3:
                break  
            else:
                print('Select correct option (1/2/3)')
        except Exception as e:
            print('Please enter a valid digit!')

 