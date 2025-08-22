import re

admin = "tristanpogi123"
admin_password = "dwightramos"

accounts = []
#full_name
#email
#password

def add_account():
        print('')
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        email = input("Enter your email: ")

        while True:
            if re.fullmatch(email_pattern, email):
                    print('')
                    print("Email format is valid. Please enter the following informations.")
                    print('')
            
                    for account in accounts:

                        if account["email"] == email:
                            print("Email already exists!")
                            break

                    full_name = input("Enter your Name: ").strip()
                    password = input('Enter your password, it should be 8 characters long: ')
                    len(password) >= 8

                    if (password) and len(password) >= 8:
                        print('')
                        print("Password strength is valid. Account Successfully Created.")
                        print('')

                    else:
                        print("")
                        print("Password is too weak. Please make the password 8 characters long.\n 12345678")
                        break
                    
                    accounts.append({"email": email,
                                    "full_name": full_name,
                                    "password": password
                                    })
                    
                    print('-------------------------------')
                    print(f"Your account has been created.")
                    print(f'Email: {email}')
                    print(f'Name: {full_name}')
                    print(f'Password: {password}')
                    print('-------------------------------')
                    return
                
            else:
                print("")
                print("Email format is invalid. Please follow the email format.\n example@gmail.com")
                break

    
def admin_view_account():
    if not accounts:
        print("")
        print("There are no accounts existing.")
        
    else:
        print('')
        print("\n--- Accounts: ---")
        for account in accounts:
            print(f'Email: {account["email"]}\n Full Name: {account["full_name"]}\n Password: {account["password"]}\n-----------------')
            print('')



def view_account():
    if not accounts:
        print("")
        print("There are no accounts existing.")
        
    else:
        print('')
        print("\n--- Accounts: ---")
        for account in accounts:
            print(f'Email: {account["email"]}\n Full Name: {account["full_name"]}\n-----------------')
            print('')



def view_account_info(account):
        print('')
        print("\n--- Account Info: ---")
        for account in accounts:
            print(f'Email: {account["email"]}\n Full Name: {account["full_name"]}\n Password: {account["password"]}\n---------------------')
            print('')



def admin_update_account():
    print('')
    email = input("Enter the email you want to update: ").strip().lower()

    for account in accounts:
        if account["email"] == email.lower():

                while True: 
                    print('')
                    print("[1] Update Email")
                    print("[2] Update Full Name")
                    print("[3] Update Password")
                    print("[4] Return to Main Menu")
                    print('')

                    try:
                        choice = int(input('Choose an Option: '))
                        
                        match choice:
                            case 1:
                                new_email = input("Enter a new email address: ").lower().strip()
                                account["email"] = new_email
                                print('')
                                print(f'Your email has been successfuly updated.\n New Email: {new_email}')

                            case 2:
                                new_full_name = input("Enter a new full name: ").strip()
                                account["full_name"] = new_full_name
                                print('')
                                print(f'Your Full Name has been successfuly updated.\n New Full Name: {new_full_name}')

                            case 3:
                                new_password = input("Enter a new password: ")
                                account["password"] = new_password
                                print('')
                                print(f'Your Password has been successfuly updated.\n New Password: {new_password}')

                            case 4:
                                print("")
                                print('Returning to the main menu...')
                                print('')
                                return
                                #exit()

                    except ValueError:
                        print("")
                        print("Invalid input. Please choose a number from 1-5 only.")
        
        else:
            print("")
            print("Account doesn't exists. Please input an existing account.")
            return
        


def update_account(account):
    while True: 
        print('')
        print("[1] Update Email")
        print("[2] Update Full Name")
        print("[3] Update Password")
        print("[4] Return to Main Menu")
        print('')

        try:
            choice = int(input('Choose an Option: '))
            
            match choice:
                case 1:
                    new_email = input("Enter a new email address: ").lower().strip()
                    account["email"] = new_email
                    print('')
                    print(f'Your email has been successfuly updated.\n New Email: {new_email}')

                case 2:
                    new_full_name = input("Enter a new full name: ").strip()
                    account["full_name"] = new_full_name
                    print('')
                    print(f'Your Full Name has been successfuly updated.\n New Full Name: {new_full_name}')

                case 3:
                    new_password = input("Enter a new password: ")
                    account["password"] = new_password
                    print('')
                    print(f'Your Password has been successfuly updated.\n New Password: {new_password}')

                case 4:
                    print("")
                    print('Returning to the main menu...')
                    print('')
                    return
                    #exit()

        except ValueError:
            print("Invalid input. Please choose a number from 1-5 only.")
        


def delete_account():
    print('')
    email = input("Enter the email you want to delete: ").strip().lower()
    
    for i,account in enumerate(accounts):
        # print(f"Indexx is {i} Value is {account}")


                if account["email"] == email.lower():
                    del accounts[i]
                    print(f"Account Successfully Deleted: {email}")
                    return

                else:
                    print("Account doesn't exists. Please input an existing account.")



def admin_account():
    while True:
        print("")
        print("Welcome back Dwight!")
        print("Please choose a function below!")
        print("")
        print("[1] Add New Account")
        print("[2] View Accounts")
        print("[3] Update Account")
        print("[4] Delete Account")
        print("[5] Delete All Accounts")
        print("[6] Exit")
        print("")

        try:
            choice = int(input('Choose an option: '))

            match choice:
                case 1:
                    add_account()
                case 2:
                    admin_view_account()
                case 3:
                    admin_update_account()
                case 4:
                    delete_account()
                case 5:
                    accounts.clear()
                case 6:
                    print("")
                    print("Exiting App...")
                    print("")
                    exit()
                #else:

        except ValueError:
            print("Invalid input. Please choose a number from 1-6 only.")
            continue



def login_account():
    print('')
    email = input("Enter your email account: ").strip().lower()

    if email == admin:
            password = input("Enter your password: ")

            if admin_password == password:
                admin_account()

            else:
                print('Incorrect password, please input the correct password.')
                return

    for account in accounts:

        if account["email"] == email:

            password = input("Enter your password: ")
            if account["password"] == password:
                
                while True:
                    print("")
                    print(f'Welcome back {account["full_name"]}!')
                    print("Please choose a function below!")
                    print("")
                    print("[1] View Account Information")
                    print("[2] View Existing Users")
                    print("[3] Update Account")
                    print("[4] Delete Account")
                    print("[5] Log-Out")
                    print("[6] Exit")
                    print("")

                    try:
                        choice = int(input('Choose an option: '))

                        match choice:
                            case 1:
                                view_account_info(account)
                            case 2:
                                view_account()
                            case 3:
                                update_account(account)
                            case 4:
                                accounts.remove(account)
                                print("----------------------------")
                                print("Account Successfuly Deleted!")
                                print("----------------------------")
                                return
                            case 5:
                                print("")
                                print("Logging Out...")
                                print("")
                                return
                            case 6:
                                print("")
                                print("Exiting App...")
                                print("")
                                break

                    except ValueError:
                        print("")
                        print("Invalid input. Please choose a number from 1-6 only.")
                        continue
                    
            else:
                print("")
                print('Incorrect password, please input the correct password.')
                return
        else:
            print("")
            print("Account doesn't exists. Please input an existing account.")
            return
    else:
        print("")
        print("Account doesn't exists. Please input an existing account.")
        return
    


def main(): 
    while True:
        print("")
        print("Welcome to PyAccount System!")
        print("Please choose a function below!")
        print("")
        print("[1] Sign Up")
        print("[2] Log-in")
        print("[3] Exit")
        print("")
        
        try:
            choice = int(input('Choose an option: '))

            match choice:
                case 1:
                    add_account()
                case 2:
                    login_account()
                case 3:
                    print("")
                    print("Exiting App...")
                    print("")
                    break
                    #exit()
                #else:

        except ValueError:
            print("")
            print("Invalid input. Please choose a number from 1-3 only.")
            continue



main()