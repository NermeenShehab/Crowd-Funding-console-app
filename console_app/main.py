from user import User
from projectMenu import project_menu

user = User()
user_loggedIn = None

while True:
    menu = '''
        ************ 😊 Welcome to Nermeen Console 😊 ************** 
        1) register 😃 
        2) login 😎
        3) exit 🏃
        '''
    print(menu)
    try:
        option = int(input('\n\nEnter your choice: 🤠 '))
    except:
        ('\n\n Invalid Option 😰.')
    if option == 1:
        user.register()
        break
    elif option == 2:
        user.login()
        user_loggedIn = user.user_loggedIn
        break
    elif option == 3:
        print('\n\n Good Bye 😍 👋')
        exit()
    else:
        print('\n\n Invalid option 😰 . Please choose a valid one.\n')

if user_loggedIn:
    project_menu(user_loggedIn)
