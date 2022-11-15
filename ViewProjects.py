import Menu


def view_project():
    f = open("../projects.txt", 'r')
    lines = f.readlines()
    f.close()

    print("======= All Projects =======")
    counter = 1
    for line in lines:
        if line == '\n':
            break
        line = line.split(':')
        print("Project %d " % counter)
        print("Project Tittle: %s" % line[0])
        print("Project Description: %s" % line[1])
        print("Total Target: %s" % line[2])
        print("Start Date: %s" % line[3])
        print("End Date: %s" % line[4])
        print("Project Owner: %s" % line[5])
        print("___________________________________")
        counter += 1




