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
    
    
    
    
    
    
    
    
    
   
      