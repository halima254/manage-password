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