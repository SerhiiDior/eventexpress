from Locators.locators import LoginPageLocators




class Auth():

    def __init__(self, browser):
        self.browser = browser
        self.locator = LoginPageLocators

    def click_on_login_button(self):
            self.browser.click_on_element(self.locator.SIGNIN)

    def clean_login_field(self):
            self.browser.clean_element(self.locator.EMAIL_SIGNIN)

    def type_login(self, login):
            self.browser.send_keys_to_element(self.locator.EMAIL_SIGNIN,login)

    def clean_password_field(self):
            self.browser.clean_element( self.locator.PASSWORD )

    def type_pass(self, password):
            self.browser.send_keys_to_element( self.locator.PASSWORD,password )

    def press_button_signin(self):
            self.browser.click_on_element(self.locator.BUTTON_SIGIN)


