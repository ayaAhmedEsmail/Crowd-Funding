import getpass


# register method

def create_user():
    fname = input('enter your first name : ')
    lname = input('enter your last name : ')
    email = input('Enter your mail :')
    try:
        phone_num = (input('Enter your phone number :'))
        # print(phone_num)
        while len(phone_num) != 11:
            phone_num = (input('Please Enter valid phone number :'))
            if phone_num[0] == 0:
                pass
            else:
                phone_num = (input('Please Enter valid phone number :'))
                print("num:", phone_num)
    except ValueError:
        print("Please Enter valid phone number : ")

        # password = input ('Enter your password :')
    psd = input('Enter your Password :')
    conf_psd = input('Confirm your Password:')
    while conf_psd != psd:
        print(' re-write password ')
        conf_psd = getpass.getpass('Confirm your Password:')
    else:
        print('===== registration successfully ====== ')

    new_user = {"First_Name": fname, "Last_Name": lname, "Email": email, "Mobile": phone_num, "Password": psd, "Activated": True}
    # print(users)
    return new_user


# add user method

def add_user(**kwargs):
    f = open("../users.txt", 'a')
    f.write(":".join([
        kwargs["First_Name"],
        kwargs["Last_Name"],
        kwargs["Email"],
        kwargs["Mobile"],
        kwargs["Password"],
        str(kwargs["Activated"])]))
    f.write('\n')
    f.close()


def register():
    user_data = create_user()
    if user_data:
        add_user(**user_data)
        print(user_data)
        print('Registration succeeded..')
    else:
        print("Registration Failed!")
