from project import Project

def project_menu(user_loggedIn):

    project = Project(user_loggedIn)

    print(f"\n\n welcome {user_loggedIn['first_name']} 😊 to our console ")

    option = None

    while True:
        
        menu = '''
        ******************** 💻 projects 💻 ************************* 
        1) Create Project
        2) View All Projects 
        3) Edit Project
        4) Delete Project
        5) Search By Date
        6) Exit 🏃
        '''
        print(menu)
        try:
            option = int(input('\n\n Enter your choice: 🤠 '))
        except:
            ('\n\n Invalid Option 😰.')
        
        if option == 1:
            print("Create Project")
            project.create()
        elif option == 2:
            print("view All projects")
            project.view()
        elif option == 3:
            print("Edit Project")
            project.edit()
        elif option == 4:
            project.delete()
        elif option == 5:
            print("Search By Date")
            project.search()
        elif option == 6:
            exit()
        else:
             print('\n\n Invalid option 😰 . Please choose a valid one.\n')
        option = None