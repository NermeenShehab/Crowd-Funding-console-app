import hashlib
import re
import uuid

from db import DB

db = DB()
db.connect_to_user("DB/users.json")

class User:
    def __init__(self) -> None:
        self.user_loggedIn = None

    def login(self):
        print('Login \n')
        try:
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")

            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

            data = db.get_user_data()
            if len(data) == 0 :
                print("\n You must choose register first to be able to login 😰 \n\n")
            else:
                for user_data in data:
                    if email == user_data.get('email') and hashed_password == user_data.get('password'):
                        self.user_loggedIn = user_data
                        print("\n\n login successful 👏")
                        break;
                else:
                    print("\n\nUser doesn't exist 😰, please try again\n")
                    self.register()

        except ValueError:
            print('\n\n There is no users ! 😅 , you must register')
    



    def register(self):
        print('Registration \n')
        try :
            first_name = input("First name : ")
            while  not first_name.isalpha() or not first_name:
                first_name = input("Enter valid First name : 😅")    
            last_name = input("Last name : ")
            while  not last_name.isalpha() or not last_name:
                last_name = input("Enter valid Last name : 😅 ")
            email = input("Enter your email : ")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            while not (re.fullmatch(regex, email)):
                email = input(" please, Enter valid email : 😅 ") 
            password = input("Password : ")
            while not password:
                password = input("Enter valid Password : 😅 ")
            confirm_password = input("Confirm password : ")
            while password != confirm_password:
                confirm_password = input("confirm Password must be match : 😅")                                  
            
            mob_regex = "^01[0125][0-9]{8}$"
            mobile_phone = input("Mobile phone : ")
            while not (re.fullmatch(mob_regex, mobile_phone)):
                mobile_phone = input("Enter valid Mobile phone : 😅")

            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        

            user_data = {
                'user_id': int(uuid.uuid1()),
                'first_name': first_name,
                'last_name': last_name,
                'email': email, 
                'password': hashed_password,
                'mobile_phone': mobile_phone
                }         

            data = db.get_user_data()

            data.append(user_data)

            db.set_user_data(data)
           
            print("\n\n registration successful 👏")
            
        except ValueError:
            print('\n\n something wrong 😅 , please try again')