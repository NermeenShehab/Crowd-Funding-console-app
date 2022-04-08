
import time
import uuid
from pprint import pprint

from db import DB

db = DB()
db.connect_to_project("DB/projects.json")

class Project:
    def __init__(self, user_loggedIn) -> None:
        self.user_id = user_loggedIn['user_id']

    def create(self):
        self.title = input("Title : ")
        while  not self.title.isalpha() or not self.title:
            self.title = input(" Enter valid Title : 😅")  
        self.details = input("Details: ")
        while  not self.details.isalpha() or not self.details:
            self.details = input("Enter valid Details: 😅")
        self.total_target = input("Total target $ : ")
        while  self.total_target.isalpha() or not self.total_target:
            self.total_target = input("Enter valid Total target $ : 😅")
        self.start_time = input("Start Date (mm/dd/yyyy) : ")
        self.end_time = input("End Date (mm/dd/yyyy) : ")           
        
        try : 
            start_date_format = time.strptime(self.start_time, '%m/%d/%Y')
            end_date_format = time.strptime(self.end_time, '%m/%d/%Y')      
            
            if start_date_format and end_date_format:
            
                project_data = {
                    "id": int(uuid.uuid1()),
                    "title": self.title,
                    "details": self.details,
                    "total_target": self.total_target,
                    "start_time": self.start_time,
                    "end_time": self.end_time,
                    "user_id": self.user_id
                    }         
                data = db.get_project_data()
                data.append(project_data)
                db.set_project_data(data)

                print('\n\n Your project is created successfully 👏 \n')
            else :
                print("\n\n Your date is invalid , please enter valid date 😅 :\n")
        except ValueError:
            print('\n\n Invalid Date! 😓 , Enter valid Date\n')

        
        

    def view(self):
        data = db.get_project_data()
        if len(data) == 0 :
            print("\n\nyou don't have project 😱\n") 
        else:
            for project in data:
                if self.user_id == project["user_id"]:
                    print("\n\n",project)


    def edit(self):
        self.view()
        try :
            project_title = input("\n\n  Enter Project Title: ")
            data = db.get_project_data()

            if len(data) == 0 and self.user_id != project["user_id"] :
                print("\n\nyou don't have project 😱\n") 
            else:
                for index, project in enumerate(data):
                    if self.user_id == project["user_id"] and project_title == project['title']:
                        while True:
                            menu = '''
                                ******************** 💻 Edit projects 💻 ************************* 
                                1) Edit Title 
                                2) Edit Details
                                3) Edit Total Target
                                4) Edit Start Date
                                5) Edit End Date
                                6) Return back to project menu 🏃
                                '''
                            print(menu)
                            try:
                                option = int(input('\n\n Enter your choice: 🤠 '))
                            except:
                                ('\n\n Invalid Option 😰.')

                            if option == 1:
                                title = input("Enter Title: ")
                                while  not title.isalpha() or not title:
                                    title = input(" Enter valid Title : 😅")
                                data[index]['title'] = title
                            elif option == 2:
                                details = input("Enter Details: ")
                                while  not details.isalpha() or not details:
                                    details = input(" Enter valid Details : 😅")
                                data[index]['details'] = details
                            elif option == 3:
                                total_target = input("Enter Total Target: ")
                                while  total_target.isalpha() or not total_target:
                                    total_target = input("Enter valid Total target $ : 😅")
                                data[index]["total_target"] = total_target
                            elif option == 4:
                                start_time = input("Enter Start Date: ")
                                try : 
                                    start_date_format = time.strptime(start_time, '%m/%d/%Y')    
                                    if start_date_format :
                                        data[index]["start_time"] = start_time
                                    else :
                                        print("\n\n Your date is invalid , please enter valid date 😅 :\n")
                                except ValueError:
                                    print('\n\n Invalid Date! 😓 , Enter valid Date\n')
                            elif option == 5 :
                                end_time = input("Enter End Date: ")
                                try : 
                                    start_date_format = time.strptime(end_time, '%m/%d/%Y')    
                                    if start_date_format :
                                        data[index]["end_time"] = end_time
                                    else :
                                        print("\n\n Your date is invalid , please enter valid date 😅 :\n")
                                except ValueError:
                                    print('\n\n Invalid Date! 😓 , Enter valid Date\n')
                                
                            elif option == 6:
                                break
                            else:
                                print('\n\n Invalid option 😰 . Please choose a valid one.\n')    
                            db.set_project_data(data)
                else:
                    print("\n\n this project name isn't exist 😱 , please try again")
        except ValueError:
            print('\n\n Invalid date ! 😅')
   
   
   
    def delete(self):
        self.view()
        try :
            project_title = input("Enter Project Title: ")
            data = db.get_project_data()
            data_original_length = len(data)

            for index, project in enumerate(data):
                if self.user_id == project['user_id'] and project_title == project['title']:
                    data.pop(index)

            if(len(data) != data_original_length):
                db.set_project_data(data)
                print("\n\n delete project successfully 👏 \n")
            else:
                print("\n\n this project name isn't exist 😱  please try again \n")
        except ValueError:
            print('\n\n Invalid data ! 😅')


            
    def search(self):
        self.view()
        data = db.get_project_data()
        if len(data) == 0 :
            print("\n\nyou don't have project 😱\n") 
        else:
            date = input("\n\n Enter Date ")

            found = False
            for project in data:
                if (date == project['start_time'] or date == project['end_time']) and self.user_id == project['user_id']:
                    found = True
                    print(project)
                    print("\n")

            if not found:
                print("\n\n Not Found!😢😢 !! you don't have project with this date 😱 ")


    

