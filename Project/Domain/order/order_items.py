
from Error_handal.logger import write_logs
import json
import datetime
import time

# Main class to take order
class Restaurant_Order:
    def __init__(self, path):
        self.path = path
        self.total_balance = 0
        self.store_order_name=[]
        

        # Load menu from file
        with open(self.path, 'r') as file:
            self.load_menu_details = json.load(file)

    # Main order method
    def order(self):
        while True:
            self.name=input('Enter your name: ')
            if self.name.isalpha():
                break
            else:
                print('Enter only characters')    
        
        while True:
            print()
            print('=' * 30)
            print('1. Breakfast item order...')
            print('2. Lunch item order...')
            print('=' * 30)

            try:
                order_menu = input('Please select any option: ')
                print()

                if order_menu.isdigit():
                    order_menu = int(order_menu)

                    # Breakfast order
                    if order_menu == 1:
                        print(f'{'ID':<10} {'Item Name':<24} {'Type':<15} {'Price':<10}')
                        print()
                        print('-'*60)
                        for n in self.load_menu_details[0]:
                            print(f"{n['id']:<10} {n['name']:<24} {n['type']:<15} {n['price']:<10} ")
                            print()
                            print('-'*60)
                        print('='*60)    
                        self.date = datetime.datetime.now()
                        self.list1 = self.load_menu_details[0]

                        while True:
                            
                            
                            self.order_item =input('Enter Item ID: ')
                            
                            # if self.order_item.isalpha():
                                #  self.order_item=int(self.order_item)
                            
                            self.count_plate=(input('Enter your quantity : '))
                            if self.count_plate.isdigit():
                                self.count_plate=int(self.count_plate)
                                print()
                                confirm_order = input('This Order is Confirm  (yes/no): ')
                                print()
                                if confirm_order.lower() == 'yes':
                                    print('Order searching', end='')
                                    for n in range(5):
                                        time.sleep(1)
                                        print('.', end='')
                                    print()

                                    found = False
                                    for order in self.list1:
                                        for key, value in order.items():
                                            if key == 'id':
                                                if value == self.order_item:
                                            
                                            
                                            
                                                    print('Order is successfully')
                                                    print()
                                                    self.total_balance += order['price']*self.count_plate
                                                    self.amount=order['price']*self.count_plate
                                                    self.itme_name=order['name']
                                                    self.confirm_data = {
                                                        'user_name':self.name,
                                                        'item_id':self.order_item,
                                                        'Item_name': self.itme_name,
                                                        'Quantity':self.count_plate,
                                                        'datetime': str(self.date),
                                                        'Order': 'confirm',
                                                        
                                                        'price':self.amount
                                                    }
                                                    self.store_order_name.append(self.confirm_data)
                                                    self.save_order_details.append(self.confirm_data)
                                                    found = True
                                                    break
                                    if not found:
                                        print('Item not available!')
                                else:
                                    print('Your order is canceled!')
                                    self.cancel_data = {
                                        'user_name':self.name,
                                        'Item_name': self.order_item,
                                        'datetime': str(self.date),
                                        'Order': 'cancel'
                                    }
                                    self.save_order_details.append(self.cancel_data)
                            else:
                                print('Enter your digit number!')        
                        
                            
                        
                            while True:        
                                ask_order = input('Order more? (yes/no): ')
                                if ask_order.isalpha():
                                    if ask_order.lower() =='yes':
                                        break
                                    elif  ask_order.lower() =='no':
                                        break
                                    else:
                                        print('Enter your only (yes/no)')
                                else:
                                    print('enter your only (yes/no)!')
                            if ask_order.lower() == 'yes':
                                continue
                            elif ask_order.lower() =='no': 
                                break       

                    # Lunch order
                    elif order_menu == 2:
                        print(f'{'ID':<10} {'Item Name':<24} {'Type':<15} {'Price':<10}')
                        print()
                        print('-'*60)
                        for n in self.load_menu_details[1]:
                            print(f"{n['id']:<10} {n['name']:<24} {n['type']:<15} {n['price']:<10} ")
                            print()
                            print('-'*60)
                        print('='*60)    
                        self.date = datetime.datetime.now()
                        self.list2 = self.load_menu_details[1]

                        while True:
                            
                            
                                
                            self.order_item = input('Enter Item ID: ')
                            
                            
                            self.count_plate=(input('Enter your quantity : '))
                            if self.count_plate.isdigit():
                                self.count_plate=int(self.count_plate)
                                print()
                                confirm_order = input('This Order is Confirm  (yes/no): ')
                                print()
                                if confirm_order.lower() == 'yes':
                                    print('Order searching', end='')
                                    for n in range(5):
                                        time.sleep(1)
                                        print('.', end='')
                                    print()

                                    found = False
                                    for order in self.list2:
                                        for key, value in order.items():
                                            
                                            if key == 'id':
                                                if value == self.order_item:
                                                    
                                            
                                                    print('Order is successfully')
                                                    print()
                                                    self.total_balance += order['price']*self.count_plate
                                                    self.amount=order['price']*self.count_plate
                                                    self.itme_name=order['name']
                                                    self.confirm_data = {
                                                        'user_name':self.name,
                                                        'item_id':self.order_item,
                                                        'Item_name': self.itme_name,
                                                        'Quantity':self.count_plate,
                                                        'datetime': str(self.date),
                                                        'Order': 'confirm',
                                                        
                                                        'price':self.amount
                                                    }
                                                    self.store_order_name.append(self.confirm_data)
                                                    self.save_order_details.append(self.confirm_data)
                                                    found = True
                                                    break
                                    if not found:
                                        print('Item not available!')
                                else:
                                    print('Your order is canceled!')
                                    self.cancel_data = {
                                        'user':self.name,
                                        'Item_name': self.order_item,
                                        'datetime': str(self.date),
                                        'Order': 'cancel'
                                    }
                                    self.save_order_details.append(self.cancel_data)
                                
                                        
                            else:
                                print('Enter your digit number!')
                                        
                        
                        
                            
                            while True:        
                                ask_order = input('Order more? (yes/no): ')
                                if ask_order.isalpha():
                                    if ask_order.lower() =='yes':
                                        break
                                    elif  ask_order.lower() =='no':
                                        break
                                    else:
                                        print('Enter your only (yes/no)')
                                else:
                                    print('enter your only (yes/no)!')
                            if ask_order.lower() == 'yes':
                                continue
                            elif ask_order.lower() =='no': 
                                break       
                    else:
                        print('Enter 1 or 2 only!')
                else:
                    print('Invalid input. Use number!')
                    

            except Exception as e:
                date = datetime.datetime.now()
                error_list = {
                    'error': str(e),
                    'function name': "order",
                    'class name': 'Restaurant_Order',
                    'datetime': date
                }
                write_logs(str(error_list))
                print('Technical issue. Please wait!')

            # Ask to go back
            while True:        
                back_to_menu = input('Back_to_menu? (yes/no): ')
                if back_to_menu.isalpha():
                    if back_to_menu.lower() =='yes':
                        break
                    elif  back_to_menu.lower() =='no':
                        break
                    else:
                        print('Enter your only (yes/no)')
                else:
                    print('enter your only (yes/no)!')
            if back_to_menu.lower() == 'yes':
                continue
            elif back_to_menu.lower() =='no': 
                break       


class Save_Order(Restaurant_Order):
    # Load order history
    def load(self, path):
        self.order_path = path
        try:
            with open(self.order_path, 'r') as file:
                self.save_order_details = json.load(file)
        except Exception as e:
            self.save_order_details = []

    # Save order history
    def save_details(self):
        with open(self.order_path, 'w') as file:
            json.dump(self.save_order_details, file, indent=4)
