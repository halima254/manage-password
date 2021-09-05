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
        
class TestCredentials(unittest.TestCase):
    """
        A test class defining test cases for credentials class

    """ 
    def setUp(self):
        """
        this method runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('gmail','halimay','halima@21')
        
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized properly
        """
        self.assertEqual(self.new_credential.account,'gmail')
        self.assertEqual(self.new_credential.userName,'halimay')
        self.assertEqual(self.new_credential.password,'halima@21')
        
    def save_credential_test(self):
        """
        test case to test if the credential object is saved into the credentials list.

        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

        
    def tearDown(self):
        '''
        method that does clears tests that have been run
        '''
        Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("facebook","halima20","asdfg11") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_delete_credential(self):
        """
        test method to test if we can remove account credentials from  credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("facebook","halima20","asdfg11")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("facebook","halima20","asdfg11") 
        test_credential.save_details()

        my_credential = Credentials.find_credential("facebook")
         
        self.assertEqual(my_credential.account,test_credential.account)
        
    def test_credential_exist(self):
        """
        test to check if we can return a boolean based on whether we the credential or not
        """
        self.new_credential.save_details()
        the_credential = Credentials("facebook", "halima20", "asdfg11")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("facebook")
        self.assertTrue(credential_is_found)
        
    def test_display_all_saved_credentials(self):
        '''
        this method displays all credentials saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
    def test_generate_Password(self): 
      '''
        test_save_credentials method saves credential objects into credential_list
      ''' 
      self.assertEqual(len(Credentials.generate_Password()),8)  