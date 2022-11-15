import CreateProject
import DeleteProject
import EditProject
import ViewProjects


def login():
    email = input('Enter your Email : ')
    password = (input('Enter your Password :'))
    user = get_user(email, password)
    if user:
        print("Login succeeded..")
        return email
    else:
        print("Login Failed!")
        return 0


# get users
def get_user(email, password):
    f = open("../users.txt", 'r')
    lines = f.readlines()
    f.close()
    found = False
    for line in lines:
        tmp = line.split(':')
        if tmp[2] == email and tmp[4] == password and tmp[5] == "True\n":
            found = True
            user = {
                "First_Name": tmp[0],
                "Last_Name": tmp[1],
                "Email": tmp[2],
                "Mobile": tmp[3],
                "Password": tmp[4],
                "Activated": tmp[5]}
    if found:
        return user
    return{}


def login_menu():
    print('------------ LOGIN ------------')
    user_mail = login()
    if user_mail:
        while True:
            ch = int(input("""
                1- Create new project
                2- View all projects
                3- Edit project
                4- Delete project
                5- Exit
                """))

            if ch == 1:
                CreateProject.create_project(user_mail)
            if ch == 2:
                ViewProjects.view_project()
            if ch == 3:
                EditProject.edit_project(user_mail)
            if ch == 4:
                DeleteProject.delete_proj(user_mail)
            elif ch == 5:
                print("Exit..")
                return 0



