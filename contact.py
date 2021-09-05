import pyperclip
import random
class Contact:
    '''
    class contacts generates new instances of a class
    '''
    

    contact_list = []
    def __init__(self, user_name, password):
        
        '''
        __init__ method helps in defining properties for our objects.

        Args:
            user_name : New contact user name.
            password: New contact password.
           
        '''
        self.user_name = user_name
        self.password= password

    def save_contact(self):
        '''
        save contact object into contact list
        '''
        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact list
        '''
        Contact.contact_list.remove(self)
        
class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []       
    @classmethod
    def verify_contact(cls,user_name, password):
        """
        method to verify whether the user is in the contact_list or not
        """
        a_cont = ""
        for user in Contact.contact_list:
            if(contact.user_name == user_name and contact.password == password):
                    a_cont == contact.user_name
        return a_cont    
    
    
    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.user_name = userName
        self.password = password
        
        
    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password

    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
    
    
    
    
    
    
    
    
   
      