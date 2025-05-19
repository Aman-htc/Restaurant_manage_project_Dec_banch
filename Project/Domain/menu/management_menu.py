    
    
    
import json
import datetime
from All_path.path import Menu_path
from Report.check_details import all_data_check
from Error_handal.logger import write_logs
from Domain.menu.restaurant_menu import check_menu
import uuid
class Restaurant_Menu:
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
            
        

            # Define Breakfast menu
            self.Breakfast_menu = [
                    {'id':uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Aloo Paratha', 'price': 50},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Aloo Paratha', 'price': 30},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Chana Ghugni', 'price': 40},
                    {'id':uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Chana Ghugni', 'price': 20},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Sattu Paratha', 'price': 50},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Sattu Paratha', 'price': 30},
                    {'id': uuid.uuid4().hex[:2] , 'type': '100g', 'name': 'Jalebi', 'price': 40},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Chai', 'price': 20},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Salad', 'price': 40},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Salad', 'price': 20},
                    {'id':uuid.uuid4().hex[:2] , 'type': '1ltr', 'name': 'Water Bottle', 'price': 20},
                    {'id':uuid.uuid4().hex[:2] ,'type': 'full','name':'Chola Bhatura','price':70},
                    {'id':uuid.uuid4().hex[:2] ,'type':'full','name':'Mix Sabji','price':50}
                ]

            # Define Lunch menu
            self.Lunch_menu = [
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Litti Chokha', 'price': 60},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Litti Chokha', 'price': 30},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Rice Dal', 'price': 70},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Rice Dal', 'price': 40},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Paneer Butter Masala', 'price': 200},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Paneer Butter Masala', 'price': 110},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Shahi Paneer', 'price': 180},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Shahi Paneer', 'price': 100},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Plain Rice', 'price': 50},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Roti (2 pcs)', 'price': 50},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'full', 'name': 'Kadhi Chawal', 'price': 120},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Kadhi Chawal', 'price': 70},
                    {'id': uuid.uuid4().hex[:2] , 'type': 'half', 'name': 'Salad', 'price': 20},
                    {'id': uuid.uuid4().hex[:2] , 'type': '1ltr', 'name': 'Water Bottle', 'price': 20},
                    {'id':uuid.uuid4().hex[:2] ,'type':'full','name':'Mix Sabji','price':50},
                    {'id':uuid.uuid4().hex[:2] , 'type': 'full','name':'Dahi','price':80},
                    {'id':uuid.uuid4().hex[:2] , 'type': 'half','name':'Dahi','price':40}
                ]

            # Append both menus to the main list
            self.menu_list.append(self.Breakfast_menu)
            self.menu_list.append(self.Lunch_menu)

        except Exception as e:
            date = datetime.datetime.now()
            error_list = {'error': str(e), 'function_name': 'menu_details', 'class': 'Restaurant', 'date': date}
            write_logs(str(error_list))
            print('Technical issue please wait!')

# call Restaurant menu 
def menu_item():
    data = Restaurant_Menu(Menu_path)
    data.menu_details()
    data.save_menu_details()
    
            


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
            self.Id_Item = uuid.uuid4().hex[:2] 
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
                       
                        
                        while True:
                                           
                            self.item_list = {}
                            # self.item_Id = int(input('Enter your item id: '))
                            self.item_Id=self.Id_Item
                            self.item_name = input('Enter your item name: ')
                            
                            id_exists = False
                            for item in self.menu_details[0]:
                                
                                if item.get('name') == self.item_name:
                                    
                                    id_exists = True
                                    break

                            if  id_exists:
                                print('This item is available . Not added.')
                            else:
                                # self.item_name = input('Enter your item name: ')
                                self.item_price = int(input('Enter your item price: '))
                                self.item_category = input('Enter your type (haph ya full): ')
                                self.item_list['id'] = self.item_Id
                                self.item_list['name'] = self.item_name
                                self.item_list['price'] = self.item_price
                                self.item_list['type'] = self.item_category
                                self.menu_details[0].append(self.item_list)
                                print('Item added successfully!')
                                break
                        # Save updated menu to file
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)
                            

                    # Add item to lunch menu
                    elif staff == 2:
                        
                        while True: 
                            self.item_list = {}  
                            self.item_Id=self.Id_Item
                            self.item_name = input('Enter your item name: ')
                            
                            id_exists = False
                            for item in self.menu_details[1]:
                                
                                if item.get('name') == self.item_name:
                                    
                                    id_exists = True
                                    break

                            if  id_exists:
                                print('This item is available. Not added.')
                            else:
                                # self.item_name = input('Enter your item name: ')
                                self.item_price = int(input('Enter your item price: '))
                                self.item_category = input('Enter your type (haph ya full): ')
                                self.item_list['id'] = self.item_Id
                                self.item_list['name'] = self.item_name
                                self.item_list['price'] = self.item_price
                                self.item_list['type'] = self.item_category
                                self.menu_details[1].append(self.item_list)
                                print('Item added successfully!')
                                break

                        # Save updated menu to file
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)

                    # Remove item from breakfast menu by index
                    elif staff == 3:
                        
                        while True:
                            
                            self.Id_number =input('Enter item Id number to remove: ')
                            found=False
                            for item in self.menu_details[0]:
                                for key,value in item.items():
                                    if key == 'id':
                                        if value == self.Id_number:
                                            self.menu_details[0].remove(item)
                                            print('remove items successfully!')
                                            found=True
                                           
                            if not found:
                                print('NO id match!') 
                            else:
                                break                      
                            

                        # Save only breakfast menu to file
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)  

                    # Remove item from lunch menu by index
                    elif staff == 4:
                        
                        while True:
                            self.Id_number =input('Enter item Id number to remove: ')
                            found=False
                            for item in self.menu_details[1]:
                                for key,value in item.items():
                                    if key == 'id':
                                        if value == self.Id_number:
                                            self.menu_details[1].remove(item)
                                            print('remove items successfully!')
                                            found=True
                                           
                            if not found:
                                print('NO id match!') 
                            else:
                                break       
                        # # Save full menu again
                        with open(self.path, 'w') as file:
                            json.dump(self.menu_details, file, indent=4)

                    elif staff == 5:
                        break  
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
        print('3. Check menu details..')
        print('4. Exit...')
        print('=' * 20)
        
        try:
            input_number = int(input('Select any option: '))
            if input_number == 1:
                # menu_item()
                # Open item manager
                item_manage()  
            elif input_number == 2:
                all_data_check()  
            elif input_number == 3:
               check_menu()
            elif input_number == 4:
                break  
            else:
                print('Select correct option (1/2/3)')
        except Exception as e:
        
            error_list={'error':str(e),'funcation name':'manage_and_report()'}
            write_logs(str(error_list))
            
            print('Technical issue please wait!')

 