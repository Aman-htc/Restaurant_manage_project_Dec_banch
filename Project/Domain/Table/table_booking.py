



from All_path.path import table_path,table_booked_details

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
                {'Table_no': 1, 'Available_seat': 5, 'Booking_time': None,"Cancelled_time":None,'Book_seat':None,},
                {'Table_no': 2, 'Available_seat': 5, 'Booking_time': None,"Cancelled_time":None,'Book_seat':None},
                {'Table_no': 3, 'Available_seat': 5, 'Booking_time': None,"Cancelled_time":None,'Book_seat':None},
                {'Table_no': 4, 'Available_seat': 5, 'Booking_time': None,"Cancelled_time":None,'Book_seat':None},
                {'Table_no': 5, 'Available_seat': 5, 'Booking_time': None,"Cancelled_time":None,'Book_seat':None}
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
                    if current_time - booking_time > timedelta(minutes=120):
                        booked_seats = 5 - table['Available_seat']
                        table['Available_seat'] += booked_seats
                        table['Booking_time'] = None

            with open(self.table_path, 'w') as file:
                json.dump(self.load_table, file, indent=4)

        def read_table(self,booked_path):
            self.table_booke=booked_path
        
            try:
                with open(self.table_booke,'r') as file:
                    self.load_table_booked=json.load(file)
            except Exception as e:
                self.load_table_booked=[]        
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
                                    booking_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    table['Booking_time']=booking_time
                        
                                    booking_dt = datetime.strptime(table['Booking_time'], "%Y-%m-%d %H:%M:%S")
                                    cancel_time = booking_dt + timedelta(minutes=120)
                                    table['Cancelled_time'] = cancel_time.strftime("%Y-%m-%d %H:%M:%S")
                                   
                                    print('Seat  confirm successfully!')
                                    self.confirm_seat={'name':self.input_name,'book_seat':self.input_seat_no,'table_no':self.input_table_no ,'datetime': booking_time }
                                    self.load_table_booked.append(self.confirm_seat)
                                    found = True
                                    order_item_generate_bill()
                                
                                       
                    
                        if not found:
                            print("There is no seat available at this table!")
                            print()
                            self.ask_book=input('Would you like to book another table(yes/no): ')
                            if self.ask_book.lower()=='yes':
                                continue
                            elif self.ask_book.lower() == 'no':
                                break
                           
                            
                        else:
                            
                            break
                            
                    else:
                        print('enter your digit number!')    
                else:
                    print('enter your digit number!')
            with open(self.table_path, 'w') as file:
                json.dump(self.load_table, file, indent=4)
                
            with open(self.table_booke,'w') as file:
                json.dump(self.load_table_booked,file,indent=4)    

        def desplay_table(self):
            
            
            
            self.clean_expired_bookings()

            with open(self.table_path, 'r') as file:
                self.table_seat = json.load(file)

            print("\n Current Table Status:")
            print(f'{"Table no":<15} {"Total seat":<15} {"Available seat":<20} {"Booking Time":<22} {"Cancelled Time"}')
            print('*' * 95)

            for table in self.table_seat:
                print(f"{table['Table_no']:<15} {'5':<15} {table['Available_seat']:<20} {str(table.get('Booking_time')):<22} {str(table.get('Cancelled_time'))}")

    except Exception as e:
        error_list={'error':str(e),'class_name':'Table_Booking'}
        write_logs(str(error_list))
        print('Technical issue please wait!')

# ---------------- Function to Book Table ----------------
def booked_table():
    obj = Table_Booking(table_path)
    obj.desplay_table()
    obj.read_table(table_booked_details)


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
                    
                    
                    break    
                elif select_option == 2:
                    tableset()
                
                elif select_option == 3:
                    break
                else:
                    print('Please select option 1, 2, or 3.')
            else:
                print('Please enter a valid number.')
    except Exception as e:
        error_list={'error':str(e),"funcation name":'table_cancel_booked()'}
        write_logs(str(error_list))
        print('Technical issue please wait!')


