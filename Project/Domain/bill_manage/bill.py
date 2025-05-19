
from Error_handal.logger import write_logs
from Domain.order.order_items import Save_Order
from All_path.path import Menu_path, Save_order_path, Load_amount_path
import json
import datetime

# Save_Amount class extends Save_Order, which extends Restaurant_Order
class Save_Amount(Save_Order):  
    
    # Load previous bill/payment data from the JSON file
    def load_amount(self, path):
        self.amount_path = path
        try:
            with open(self.amount_path, 'r') as file:
                self.bill_amount_list = json.load(file)  
        except Exception as e:
            self.bill_amount_list = []  

    # Handle bill calculation, display, and payment collection
    def amount_details(self):
        try:
            while True:
                   # If no items were ordered, skip billing
                if self.total_balance == 0:
                 
                    break
                else:
                    self.add_amount = {}
                    # GST rate fixed at 10%
                    self.gst_rate = 10  
                    print()
                    print('This is your bill sir/madam')
                    print('=' * 30)
                    print()
                    
                    print('Customer Name: ',self.confirm_data["user_name"])
                    self.name=self.confirm_data['user_name']
                    
                    print(f'{'Quantity':<10} {'Item_name':<15} {'price'}')
                    print('-'*40)
                    for n in self.store_order_name:
                        print(f'{n['Quantity']:<10}{n['Item_name']:<15}{n['price']}')
                        print('-'*40)
                    print()    
                    

                    print('All Items Amount is :', self.total_balance)
                    print('GST:', self.gst_rate)

                    # Calculate GST and final amount
                    gst_amount = self.total_balance * self.gst_rate / 100
                    Total_amount = self.total_balance + gst_amount

                    print('GST Amount:', gst_amount)
                    print('Total Balance : ', Total_amount)
                    print('=' * 30)
                    print()
                    print('*'*20)
                    print('1. online payment!')
                    print('2. cash payment!!')
                    print('*'*20)
                    print()
                    enter_option=(input('Select any option: '))
                    if enter_option.isdigit():
                        enter_option = int(enter_option)
                        if enter_option == 1:
                        
                    
                            # Ask for UPI number
                            self.upi_number = input('Enter your UPI number: ')
                            if len(self.upi_number) == 10:
                                if  self.upi_number.count(self.upi_number[0]) != 10:
                                    
                                    # Prepare the bill dictionary to save
                                    self.add_amount['Customer_name']=self.name
                                    self.add_amount['gst amount'] = gst_amount
                                    self.add_amount['Total amount'] = Total_amount
                                    self.add_amount['upi'] = self.upi_number
                                    self.add_amount['datetime'] = str(self.date)
                                    self.add_amount['payment']='online'

                                    # Ask for payment
                                    self.money = input('Please enter your money: ')
                                    if self.money.isdigit():
                                        self.money = float(self.money)

                                        # Check if paid amount is correct
                                        if self.money == Total_amount:
                                            self.bill_amount_list.append(self.add_amount)

                                            print('Payment Successfully!')
                                            print()
                                            print('Thanks')
                                            print()
                                            break
                                        else:
                                            print('Please enter the exact total amount')  
                                    else:
                                        print('Only numeric values are allowed!')  
                                else:
                                    print('correct upi number!')          
                            else:
                                print('Enter a 10-digit UPI number!')
                                
                        elif enter_option == 2:
                            
                                
                            self.money = input('Please enter your money: ')
                            if self.money.isdigit():
                                self.money = float(self.money)
                                if self.money == Total_amount:
                                
                                    self.add_amount['Customer_name']=self.name
                                    self.add_amount['gst amount'] = gst_amount
                                    self.add_amount['Total amount'] = Total_amount
                                
                                    self.add_amount['datetime'] = str(self.date)
                                    self.add_amount['payment']='cash'
                                    self.bill_amount_list.append(self.add_amount)
                                    print('payment is successfully')
                                    print()
                                    print('Thanks')
                                    break
                                else:
                                    print('Please enter the exact total amount')    
                            else:
                                print('Only numeric values are allowed!')      
                    else:
                        print('enter your only digit number!')
                        
                                
        except Exception as e:
            # Log any technical error
            date = datetime.datetime.now()                
            error_data = {
                'error': str(e),
                'function': 'amount_details',
                'class': 'Save_Amount',
                'date': date
            }
            write_logs(str(error_data))
            print('Technical issue, please wait!')

    # Save the bill/payment data to file
    def save_amount_details(self):
        with open(self.amount_path, 'w') as file:
            json.dump(self.bill_amount_list, file, indent=4)

# This function handles the entire process: loading data, taking order, billing, and saving
def order_item_bill_details():
    data = Save_Amount(Menu_path)             
    data.load(Save_order_path)                
    data.load_amount(Load_amount_path)        
    data.order()                              
    data.amount_details()                    
    data.save_details()                       
    data.save_amount_details()               

# Ask user if they want to order, and handle accordingly
def order_item_generate_bill():
    while True:
        print()
        print('*' * 40)
        order = input('Can I order something, please: (yes/no): ')
        if order.lower() == 'yes':
            
            # Call the main ordering & billing function
            order_item_bill_details() 
            break 
        else:
            break
       