import unittest
from contact import Contact, Credentials
import pyperclip


class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
     here contact displays the user
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method that runs each test cases.
        '''
        self.new_contact = Contact("halima","2021") # create contact object

    def test_init(self):
        '''
        test_init test case that tests if the object is correctly initialized
        '''

        self.assertEqual(self.new_contact.user_name,"halima")
        self.assertEqual(self.new_contact.password,"2021")
        
    def test_save_contact(self):
        """
        test case to test if a new user instance has been saved to the Contact list

        """
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)