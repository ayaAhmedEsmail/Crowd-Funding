

def edit_project(user_mail):
    print("--------------- Edit Project --------------------")
    title = input("Enter project name you want to edit: ")
    file = open("../projects.txt", 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        if line.split(":")[0] == title:
            print(line)
            print(line[-1].split(':'))
            del lines[lines.index(line)]  # delete the line and take it with new modification

            # enter here the editing method ! select a field you want to edit then enter your modification

            title = input("Enter Project title: ")
            details = input("Enter Project details: ")
            target = input("Enter Project total target: ")
            start_date = input("Enter Project start date (date format DD-MM-YYYY like): ")
            end_date = input("Enter Project end date (date format like DD-MM-YYYY): ")

            lines.append(title + ":" + details + ":" + target + ":" + start_date + ":" + end_date + ":" + user_mail)
            file = open("../projects.txt", "a")
            file.writelines(lines)
            file.close()

            print("Project Edited !")
        else:
            print("Sorry You can only edit Your own projects !")
    file = open("../pro.txt", 'w')
    file.writelines(lines)
    file.close()
