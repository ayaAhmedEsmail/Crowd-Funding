import datetime


def save_project(**kwargs):
    f = open('../projects.txt', 'a')
    f.write(":".join([kwargs["Title"],
                      kwargs["Details"],
                      kwargs["Total_Target"],
                      kwargs["Start_Time"],
                      kwargs["End_Time"],
                      kwargs["User"]]))
    f.write('\n')
    f.close()
    print('Project created..')


def create_project(user_amil):
    project = valid_project(user_amil)

    if project:
        save_project(**project)
    else:
        print("Project not saved, try again")


def valid_time(date):

    d, m, y = date.split('/')
    date_format = '%d/%m/%Y'
    # using try-except blocks for handling the exceptions
    try:
        # formatting the date using strptime() function
        date_object = datetime.datetime(int(y), int(m), int(d))

        print(date_object)
        valid_date = True

    # If the date validation goes wrong
    except ValueError:

        # printing the appropriate text if ValueError occurs
        print("Incorrect data format, should be DD-MM-YYY")
        valid_date = False

    if valid_date:
        return date
    else:
        print("Incorrect data format, should be DD-MM-YYY")
        return 0


def valid_project(user_mail):
    title = input("Project Title: ")
    if ':' in title:
        pass
    if title:
        details = input("Project Details: ")
        total_target = input("Project Target: ")
        if total_target:
            start_date = valid_time(input("Start Date (dd/mm/yy): "))
            if start_date:
                end_date = valid_time(input("End Date (dd/mm/yy): "))
                if end_date:
                    project = {"Title": title,
                               "Details": details,
                               "Total_Target": total_target,
                               "Start_Time": start_date,
                               "End_Time": end_date,
                               "User": user_mail}
                    return project
    else:
        print("Title Can't be empty, pls try again..")

    return False
