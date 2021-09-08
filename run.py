#!/usr/bin/env python3.8
from contact import Contact, Credentials
from termcolor import colored

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
    Function that displays all the saved contacts
    '''
    return Contact.display_contacts()

def login_contact(user_name,password):
    """
    function that makes an existing user login
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
    Function that saves new credentials
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credentials
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a credential

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    function for finding credentials using the account name
    """
    return Credentials.find_credential(account)

def check_credentials(account):
    """
   Function that checks whether a credential of a particular user exists and returns a boolean

    """
    return Credentials.if_credential_exist(account)
def main():   
    print(colored("Dear Client, Welcome to Password Manager\n To continue, press one of the two options\n NA :   New Account  \n EA: Existing Account  \n",'blue'))
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' *40)
        username = input("user_Name: ")
        while True:
            print(" tp - To type your own pasword:\n rp - To generate a new random password")
            new_pass = input().lower().strip()
            if new_pass == 'tp':
                password = input("Your Password\n")
                break
            elif new_pass == 'gp':
                password = generate_Password()
                print(f"Your new Password is{password}")
                break
            else:
                print("Your password is invalid, Please try again")
        save_contacts(create_contact(username,password))
        print("*"*70)
        print (colored(f"Hello {username}, Your account has been created succesfully! Your password is: {password}", 'green'))
        print("*"*70)
    elif short_code == 'ha':
        print("*"*50)
        print("Enter your username and your Password to log in:")
        print('*' * 50)
        username = input("username: ")
        password = input("password: ")
        login = login_contact(username,password)
        if login_user == login:
            print (colored(f"Hello {username}.Welcome To PassWord Manager",'green'))
            print('\n')
            
    while True:
         print (colored("Use the short codes below:\n cc - Create new credentials \n dc - display credentials \n sc - Search for a credential \n rp - generate random password \n d- delete credential \n ex - exit password manager \n",'blue'))
         short_code = input().lower().strip()
         if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name:")
            account = input().lower()
            print("Your username:")
            userName = input()
            while True:
                print(" tp - To type your own pasword :\n rp - To generate random Password")
                choose_password = input().lower().strip()
                if choose_password == 'tp':
                    password = input("input your password of choice\n")
                    break
                elif choose_password == 'gp':
                    password = generate_Password()
                    break
                else:
                    print (colored("Invalid password please try again",'red'))
            
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print (colored(f"Account Credential for: {account} - Username: {userName} - Password:{password} has been created succesfully", 'green'))
            print('\n')



         elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of accounts: ")
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print (colored(f" Account:{account.account} \n user Name:{username}\n password:{password}",'green'))
                    print('_'* 30)
                print('*' * 30)
            else:
                print (colored("You have not saved any credentials",'red'))
         elif short_code == "sc":
            print("Account name you want to search")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"username: {search_credential.user_name} password :{search_credential.password}")
                print('-' * 50)
            else:
                print (colored("This credential does not exist",'red'))
                print('\n')
                
                
         elif short_code == "d":
            print("Enter the account name of the credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("The Credentials does not exist")
         elif short_code == 'gp':
            password = generate_Password()
            print (colores(f" {password} Has been generated succesfully.Please proceed to use it to your account",'blue')) 
         elif short_code == 'ex':
            print (colored("Thank you for choosing us! ",'yellow'))
            break
         else:
            print (colored("Wrong entry, ensure that they match", 'yellow'))
    else:
      print (colored("Please enter a valid input to continue",'yellow'))    

if __name__ == '__main__':
     main()