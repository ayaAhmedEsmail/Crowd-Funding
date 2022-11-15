def delete_proj(user_mail):
    print("--------------- Delete Project --------------------")
    title = input("Enter project title to delete: ")
    file = open("../projects.txt", 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        if line.split(":")[0] == title:
            print(line)
            print(line[-1].split(':'))
            # if line[-1].split(':') == user_mail:
            print(line)
            del lines[lines.index(line)]  # delete the line and take it with new modification

            file = open("../projects.txt", "a")
            file.writelines(lines)
            file.close()

            print("Project deletes !")
        else:
            print("Sorry You can not delete this project !")
    file = open("../projects.txt", 'w')
    file.writelines(lines)
    file.close()
