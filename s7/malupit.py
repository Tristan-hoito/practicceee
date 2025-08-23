import re

accounts = []
#full_name
#email
#password

def add_account():
    print('')
    email = input("Enter your email: ").strip().lower()
    #strip to remove unecessary spaces
    #lower for lower case

    for account in accounts:
        if account["email"] == email.lower():
            print("Email already exists!")
            return
    
    full_name = input("Enter your full name: ").strip()
    password = input('Enter your password: ')
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



def view_account():
    if not accounts:
        print("There are no accounts existing.")
        
    else:
        print('')
        print("\n--- Accounts: ---")
        for account in accounts:
            print(f'Email: {account["email"]}\n Full Name: {account["full_name"]}\n-----------------')
        print('')



def update_account():
    print('')
    email = input("Enter the email you want to update: ").strip().lower()

    for account in accounts:
        if account["email"] == email.lower():

            password = input("Enter your password: ")
            if account["password"] == password:

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
                
            else:
                print('Incorrect password, please input the correct password.')
                return
        
        else:
            print("Account doesn't exists. Please input an existing account.")
            return
        


def delete_account():
    print('')
    email = input("Enter the email you want to delete: ").strip().lower()
    
    for i,account in enumerate(accounts):
        # print(f"Indexx is {i} Value is {account}")

        password = input("Enter your password: ")
        if account["password"] == password:

                if account["email"] == email.lower():
                    del accounts[i]
                    print(f"Account Successfully Deleted: {email}")
                return

        else:
            print('Incorrect password, please input the correct password.')
            return

    else:
        print("Account doesn't exists. Please input an existing account.")



def main():
    while True:
        print("")
        print("Welcome to PyAccount System!")
        print("Please choose a function below!")
        print("")
        print("[1] Add New Account")
        print("[2] View Accounts")
        print("[3] Update Account")
        print("[4] Delete Account")
        print("[5] Exit")
        print("")

        try:
            choice = int(input('Choose an option: '))

            match choice:
                case 1:
                    add_account()
                case 2:
                    view_account()
                case 3:
                    update_account()
                case 4:
                    delete_account()
                case 5:
                    print("")
                    print("Exiting App...")
                    print("")
                    break
                    #exit()
                #else:

        except ValueError:
            print("Invalid input. Please choose a number from 1-5 only.")
            continue



main()