#!/usr/bin/env python3.8
from contact import Contact, Credentials

def create_contact(userName, password):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(userName,password)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()
    

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()

def login_contact(user_name,password):
    """
    function that checks whether a user exists and then login the user in.
    """
  
    check_contact = Credentials.verify_contact(user_name,password)
    return check_contact

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)

def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)
def main():   
    print("Hello Welcome to your Password Manager.\n Press one of the following to continue.\n CA ---  Create New Account  \n HA ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' *40)
        username = input("user_Name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            new_pass = input().lower().strip()
            if new_pass == 'tp':
                password = input("Enter Password\n")
                break
            elif new_pass == 'gp':
                password = generate_Password()
                print(f"Your new Password is{password}")
                break
            else:
                print("Invalid password please try again")
        save_contacts(create_contact(username,password))
        print("*"*70)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*70)
    elif short_code == 'ha':
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_contact(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Manager")
            print('\n')
            
    while True:
         print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
         short_code = input().lower().strip()
         if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                choose_password = input().lower().strip()
                if choose_password == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif choose_password == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')



         elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of accounts: ")
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet...")
         elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.user_name} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
                
                
         elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")
         elif short_code == 'gp':
            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
         elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
         else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
      print("Please enter a valid input to continue")      

if __name__ == '__main__':
     main()