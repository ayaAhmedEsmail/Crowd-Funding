import CreateProject
import Login
import Registration
import ViewProjects
import EditProject


def print_menu():
    print('\n\n\n\n'
          '================================\n '
          '              MENU\n '
          '================================\n'
          '1 - Register\n'
          '2 - Login\n'
          '================================\n'
          '3 - Exit\n'
          '================================\n'
          'Enter a choice and press enter => '
          )
    user_input = 0
    while user_input != 3:
        user_input = int(input())

        if user_input == 1:
            Registration.register()
            print_menu()
        elif user_input == 2:
            Login.login_menu()
        else:
            print(" Exiting... ")
            break


"""def home_menu():
    user_input = 0
    print('\n\n\n\n'
          '================================\n '
          '              Home Page \n '
          '================================\n'
          ' 1- Create new project\n'
          ' 2- View all projects\n'
          ' 3- Edit project\n'
          ' 4- Delete project\n'
          ' 5- Search for a project\n'
          '================================\n'
          '6 - Exit\n'
          '================================\n'
          'Enter a choice and press enter => '
          )
    while user_input != 7:
        user_input = int(input())

        if user_input == 1:
            CreateProject.create_project()
            Login.login_menu()
        elif user_input == 2:
            ViewProjects.view_project()
            Login.login_menu()
        elif user_input == 3:
            EditProject.edit_project()
        else:
            print(" Exiting... ")
            break"""
