import json
import time
import getpass
import msvcrt

from All_path.path import Sign_up_path 

from All_path.path import Staff_path

from Error_handal.logger import write_logs

from Authentication.auth_signup import  Staff_User,admin_sign

from Domain.menu.management_menu import manage_and_report

from Domain.menu.restaurant_menu import menu_details


import datetime

         
class Login_Staff:
    def __init__(self,path):
        
        try:
            self.path=path
            
        
            # Load existing user data from JSON file
            
            with  open(self.path,'r') as file:
                self.load_data=json.load(file) 
        except Exception as e:
            date=datetime.datetime.now()            
            error_data={'error':str(e),"funcation_name":'__init__()','class':'Login_User','date':date}
            write_logs(str(error_data))
            print('Technical issue please wait')
    def get_masked_password(self, prompt=''):
        print(prompt, end='', flush=True)
        password = ''
        while True:
            ch = msvcrt.getch()
            if ch in [b'\r', b'\n']:  # Enter
                print()
                break
            elif ch == b'\x08':  # Backspace
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            elif len(password) < 6:
                try:
                    password += ch.decode()
                    print('.', end='', flush=True)
                except:
                    pass
        return password
        
                    
    def input_staff(self):
        
        try:
            while True:
            
                input_data=input('please enter your email address:  ')
                found=False
                for email in self.load_data:
                    for key,value in email.items():
                        if key == 'email' and value == input_data:
                            
                            
                            found=True
                        
                if not found:
                    print('No match invalid email please try again!') 
                else:
                    break
                
                                
            while True:
                self.input_data = self.get_masked_password('Enter your 6-character password: ')
        
                print('Searching',end='')
                for n in range(5):
                    time.sleep(1)
                    print('.',end='')
                print()    
                        
                found=False
                for password in self.load_data:
                    for key,value in  password.items():
                        if key =='password':
                            if value == self.input_data:
                                
                            
                                found=True
                
                if not found:
                    print('No match invalid password please try again!') 
                else:
                   break   
            print('Login successfully!')                
        except Exception as e:
            data=datetime.datetime.now()            
            error_data={'error':str(e),"funcation_name":' input_user()','class':'Login_User','date':data}
            write_logs(str(error_data))
            print('Technical issue please wait')

# child class (Admin_Login) is created when inherits the properties of the parent class

class Admin_Login(Login_Staff):
    """The child class is inheriting the properties of the parent class and using them"""
    try:
        
        def __init__(self,path):
            self.path=path
        
            with open(self.path,'r') as file:
                self.load_data=json.load(file)
    except Exception as e:
        data=datetime.datetime.now()  
        error_data={'error':str(e),'function_name':'__init__()','class':'Admin_Login','date':data} 
        write_logs(str(error_data)) 
        print('Technical issue please wait!')
        
        
        

      
        
def login_menu():
    """When the user press number 1, an object of the parent class (Login_User) is 
     Creat and its method is executed.
     When the  user preee number 2, an object of the child class (Admin_Login) is created 
     when inherits the properties of the parent class and its method is executed"""
    while True:
        
        print('******Start login******')
        print()
        print('1.  admin login....!')
        print('2.  staff login....!')
        print('3.  Exit....')
        press_number=(input('Select any opation: '))
        if press_number.isdigit():
            press_number=int(press_number)
            if press_number == 1:
                data= Admin_Login(Sign_up_path)
                
                data.input_staff()
                print()
                manage_and_report()
                
            elif press_number == 2:
                
                data= Login_Staff(Staff_path)
                print()
                data.input_staff()
                
                # call menu and order bill details
                menu_details()
                
            elif press_number == 3:
                print('Thanks ')
                break
            else:
                print('select correct option!')
        else:
            print('Enter only digit number!')    

        
def restaurant_menu():
    while True:
        
        print('='*30)
        print()
        print('Restaurant Manegment System')
        print()
        print('='*30)
        print()
        print('1. Sign up......') 
        print('2. Login........')
        print('3. Exit')
        print()
        press_number=input('Select any option: ')
        if press_number.isdigit():
            press_number=int(press_number)
            if press_number == 1:
                print()
                
                obj = Staff_User(Staff_path)
                obj.load_user_details()
        
                obj.input_user_details()
                obj.save_user_data()

                admin_sign()
            elif press_number == 2:
                print()
                login_menu()
            elif press_number ==3:
                break 
            else:
                print('invalid number please check option!')   
        else:
            print('invalid number please try again!')                   
           
           
        
