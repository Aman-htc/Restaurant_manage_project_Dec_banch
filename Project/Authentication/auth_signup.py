
import msvcrt
import json
import uuid
import datetime
from Error_handal.logger import write_logs 
from All_path.path import Sign_up_path

class Staff_User:
    def __init__(self, path):
        self.path = path  # File path to store user data

    def load_user_details(self):
        try:
            with open(self.path, 'r') as file:
                self.data_list = json.load(file)  # Load existing user data from file
        except Exception:
            self.data_list = [] 

    def save_user_data(self):
        try:
            with open(self.path, 'w') as file:
                json.dump(self.data_list, file, indent=4)  # Save user data to file
        except Exception as e:
            data = datetime.datetime.now()
            error_data = {
                'error': str(e),
                'time': data,
                'function name': 'save_user_data()'
            }
            write_logs(str(error_data))  # Log the error
            print('Technical issue please wait!')

    def get_masked_password(self, prompt=''):
        print(prompt, end='', flush=True)
        password = ''
        while True:
            ch = msvcrt.getch()  
            if ch in [b'\r', b'\n']:  
                print()
                break
            elif ch == b'\x08':  # Backspace key
                if password:
                    password = password[:-1]  
                    print('\b \b', end='', flush=True)  
            elif len(password) < 6:
                try:
                    password += ch.decode()  
                    print('.', end='', flush=True)  
                except:
                    pass
        return password  # Return original password

    def input_user_details(self):
        try:
            while True:
                self.store_user = {} 
                # Generate unique 6-digit ID 
                self.Id_user = uuid.uuid4().hex[:6]  

                # Get staff's name
                while True:
                    self.user_name = input('please enter your name: ')
                    if self.user_name.isalpha():
                        self.store_user['id'] = self.user_name + "_" + self.Id_user
                        self.store_user['name'] = self.user_name
                        break
                    else:
                        print('enter only characters!')

                # Get staff's email
                while True:
                    self.user_email = input('please enter your email: ')
                    if '@' in self.user_email and '.' in self.user_email:
                        self.store_user['email'] = self.user_email
                        break
                    else:
                        print('enter a valid email address!')

                # Get staff's contact number
                while True:
                    self.user_contact = input('Please enter your contact number: ')
                    if len(self.user_contact) == 10 and self.user_contact.isdigit():
                        if self.user_contact.count(self.user_contact[0]) != 10:  # Reject repeated digits
                            self.store_user['contact'] = self.user_contact
                            break
                        else:
                            print("All digits are the same. Please enter a valid contact number.")
                    else:
                        print("Please enter a valid 10-digit number.")

                # Get staff's role
                while True:
                    self.role = input('Enter your role: ')
                    if self.role.lower() == 'staff':
                        self.store_user['Role'] = self.role
                        break
                    else:
                        print('Please enter only staff"!')

                # Get staff's password (masked)
                while True:
                    self.user_password = self.get_masked_password('Enter your 6-character password: ')
                    if len(self.user_password) == 6:
                        self.store_user['password'] = self.user_password
                        break
                    else:
                        print('Invalid! Enter exactly 6 characters.')

                # Add staff to list and finish sign-up
                self.data_list.append(self.store_user)
                print('Sign up successfully')
                break

        except Exception as e:
            date = datetime.datetime.now()
            error_data = {
                'error': str(e),
                'time': date,
                'function name': 'input_user_details()',
                'date': date
            }
            write_logs(str(error_data))  # Log error
            print('Technical issue please wait!')



class Admin:
    def __init__(self,path):
        self.admin_path=path
        self.admin_list=[]      
    def details_admin(self):
        self.Id_admin=uuid.uuid4().hex[:6]
        self.admin_information={}   
        self.admin_name='aman kushwaha'
        self.admin_email='aman@gmail.com'
        self.admin_contact=8102648831
        self.admin_password='810026'
        self.admin_information['id']=self.admin_name +'_'+ self.Id_admin
        self.admin_information['name']=self.admin_name
        self.admin_information['email']=self.admin_email
        self.admin_information['contact']=self.admin_contact
        self.admin_information['password']=self.admin_password
        self.admin_information['roll']='admin'
        self.admin_list.append(self.admin_information)
    def save_admin(self):
        with open(self.admin_path,'w') as file:
            json.dump(self.admin_list,file,indent=4)   

        
def admin_sign():
    data=Admin(Sign_up_path)        
    data.details_admin()
    data.save_admin()