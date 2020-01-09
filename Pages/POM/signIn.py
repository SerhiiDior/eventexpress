from Locators.locators import LoginPageLocators
from Locators.locators import RegisterLocators
from Data.credentials import *



class SignInUpClass():


    def __init__(self, browser):
        self.browser = browser
        self.locator_login = LoginPageLocators
        self.locator_reg = RegisterLocators

    #     actor - is a person with own permissions (admin or user).Method of precondition for testing
    def enter_actor(self, username, password):
        self.browser.click_on_element(self.locator_login.SIGNIN)
        self.browser.clean_element(self.locator_login.EMAIL_SIGNIN)
        self.browser.send_keys_to_element(self.locator_login.EMAIL_SIGNIN, username)
        self.browser.clean_element(self.locator_login.PASSWORD)
        self.browser.send_keys_to_element(self.locator_login.PASSWORD,password)
        self.browser.click_on_element(self.locator_login.BUTTON_SIGIN)
        print ('Login OK')

#on home page button for opening form with registration & login
    def click_sign_in_up(self):
        self.browser.click_on_element(self.locator_login.SIGNIN)









#     REGISTER FORM
    def click_on_register(self):
        self.browser.click_on_element( self.locator_reg.REGISTER )





