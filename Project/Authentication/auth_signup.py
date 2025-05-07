import json 
import uuid
import datetime
from Error_handal.logger import write_logs 

class Staff_User:
    def __init__(self,path):
        self.path=path
        
        
        
    def load_user_details(self): 
        """Load existing user data from the JSON database file"""
        try:
            with open(self.path,'r') as file:
                self.data_list=json.load(file)
        except Exception as e:
            self.data_list=[]        
    def save_user_data(self):
        """Save the current user data list in to the JSON database"""
        
        try:
            
            with open(self.path,'w') as file:
                
                json.dump(self.data_list,file,indent=4)        
        except Exception as e:
            data=datetime.datetime.now()
            error_data={'error':(str(e)),'time':data,'function name':'save_user_data()'}
            write_logs(str(error_data))
            print('Technical issue please wait!')

            
    def input_user_details(self):
        
        """
        Collect user details (name,contact,password,email,rool),
        Validation input , and store them ina dictionary with unique ID"""
        
        try:
            while True:
                    
                self.store_user={}
                # Generate a unique 6-character user ID
                self.Id_user=uuid.uuid4().hex[:6]
                while True:
                    # input Name
                    self.user_name=input('please enter your name: ')  
                    if self.user_name.isalpha():
                        self.store_user['id'] = self.user_name+"_"+self.Id_user
                        self.store_user['name'] = self.user_name
                        break
                    else:
                        print('enter your only character!') 
                    
                while True:
                    # input Email 
                    self.user_email=input('please enter your email: ')
                    if  '@' in self.user_email and '.' in self.user_email:
                        
                        self.store_user['email'] = self.user_email
                        break
                    else:
                        print('enter your correct email address!')   
                            
                while True:
                    # input Conatct Number
                    self.user_contact=(input('please enter your contact number: '))
                    if len(self.user_contact)==10:
                        if self.user_contact.isdigit():
                        
                            self.store_user['contact'] = self.user_contact
                            
                            break
                        else:
                            print('enter your only digit number!')  
                            
                    else:
                        print('enter your 10 digit number! ')  
                
                
                while True:
                    # Input Role (admin/user)
                    self.role=input('please enter your role: ').lower()  
                    if  self.role == "admin":
                        self.store_user['role']=self.role
                        break
                    elif  self.role == 'staff': 
                        
                        self.store_user['role']=self.role
                        break
                    else:
                        print('please enter your admin/user')
                        
                    
                while True:
                    # Input Password
                    self.user_password=input('please enter your password: ')
                    if len(self.user_password)==6:
                    
                        self.store_user['password']=self.user_password
                        # self.data_list.append(self.store_user)
                        # print(self.data_list)
                        
                        break
                    else:
                        print('invalid enter your six character!')
                self.data_list.append(self.store_user) 
                print('Sing up successfully')       
                ask_singup=input('Do you want to sing up aas well (yes/no): ').lower()   
                if  ask_singup !='yes':
                    break
                
        except Exception as e:
            
            date=datetime.datetime.now()
            error_data={'error':(str(e)),'time':data,'function name':'input_user_details()','date':date}
            write_logs(str(error_data))
            print('Technical issue please wait!')

            

class Admin:
    def __init__(self):
        self.admin_path=r"Restaurant_management_project/Project/Database/admin.json"
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
    data=Admin()        
    data.details_admin()
    data.save_admin()