

# # import datetime

from All_path.path import table_path

import json
from Domain.bill_manage.bill import order_item_generate_bill
from datetime import datetime, timedelta
from Error_handal.logger import write_logs

# ---------------- Table Setup Class ----------------
class Table_Set:
    try:
        
        def __init__(self,path):
            self.table_path =path
            self.total_table = [
                {'Table_no': 1, 'Available_seat': 5, 'Booking_time': None,'name':None,'Book_seat':None},
                {'Table_no': 2, 'Available_seat': 5, 'Booking_time': None,'name':None,'Book_seat':None},
                {'Table_no': 3, 'Available_seat': 5, 'Booking_time': None,'name':None,'Book_seat':None},
                {'Table_no': 4, 'Available_seat': 5, 'Booking_time': None,'name':None,'Book_seat':None},
                {'Table_no': 5, 'Available_seat': 5, 'Booking_time': None,'name':None,'Book_seat':None}
            ]

        def save_table(self):
            with open(self.table_path, 'w') as file:
                json.dump(self.total_table, file, indent=4)
    except Exception as e:
        error_list={'error':str(e),'class name': 'Table_Set'}            
        write_logs(str(error_list))
        print('Technical issue please wait!')
# call table_set 
def tableset():
    obj = Table_Set(table_path)
    obj.save_table()


# ---------------- Table Booking Class ----------------
class Table_Booking:
    try:
        
        def __init__(self,path):
            self.table_path =path

        def clean_expired_bookings(self):
            with open(self.table_path, 'r') as file:
                self.load_table = json.load(file)

            current_time = datetime.now()
            for table in self.load_table:
                if table['Booking_time']:
                    booking_time = datetime.strptime(table['Booking_time'], "%Y-%m-%d %H:%M:%S")
                    if current_time - booking_time > timedelta(minutes=10):
                        booked_seats = 5 - table['Available_seat']
                        table['Available_seat'] += booked_seats
                        table['Booking_time'] = None

            with open(self.table_path, 'w') as file:
                json.dump(self.load_table, file, indent=4)

        def read_table(self):
            self.clean_expired_bookings()

            while True:
                with open(self.table_path, 'r') as file:
                    self.load_table = json.load(file)

                print()
                self.input_name=input('Enter your name: ')
                self.input_table_no = input('Enter your table no: ')
                if self.input_table_no.isdigit():
                    self.input_table_no = int(self.input_table_no)
                    self.input_seat_no = input('Enter your seat no: ')
                    if self.input_seat_no.isdigit():
                        self.input_seat_no = int(self.input_seat_no)
                        found = False
                        for table in self.load_table:
                            if table['Table_no'] == self.input_table_no:
                                if table['Available_seat'] >= self.input_seat_no:
                                    table['Available_seat'] -= self.input_seat_no
                                    table['Booking_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    table['name']=self.input_name
                                    table['Book_seat']=self.input_seat_no 
                                    print('Seat  confirm successfully!')
                                    found = True
                                    break
                        if not found:
                            print(" Table not found or no seats!")
                        else:
                            break
                    else:
                        print('enter your digit number!')    
                else:
                    print('enter your digit number!')
            with open(self.table_path, 'w') as file:
                json.dump(self.load_table, file, indent=4)

        def desplay_table(self):
            self.clean_expired_bookings()

            with open(self.table_path, 'r') as file:
                self.table_seat = json.load(file)

            print("\n Current Table Status:")
            print(f'{"Table no":<15} {"Total seat":<15} {"Available seat"}')
            print('*'*45)

            for table in self.table_seat:
                print(f" {table['Table_no']:<15}{'5':<15}{table['Available_seat']}")
    except Exception as e:
        error_list={'error':str(e),'class_name':'Table_Booking'}
        write_logs(str(error_list))
        print('Technical issue please wait!')

# ---------------- Function to Book Table ----------------
def booked_table():
    obj = Table_Booking(table_path)
    obj.desplay_table()
    obj.read_table()


# ---------------- Main Menu Loop ----------------
def table_cancel_booked():
    try:
        
        while True:
            print('*' * 30)
            print('1. Book Table')
            print('2. Reset All Tables')
            print('3. Exit')
            print('*' * 30)
            select_option = input('Select an option: ')
            if select_option.isdigit():
                select_option = int(select_option)
                if select_option == 1:
                    booked_table()
                    order_item_generate_bill()
                elif select_option == 2:
                    tableset()
                
                elif select_option == 3:
                    break
                else:
                    print('Please select option 1, 2, or 3.')
            else:
                print('Please enter a valid number.')
    except Exception as e:
        print('Technical issue please wait!')


