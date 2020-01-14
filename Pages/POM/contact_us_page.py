from Locators.locators import ContactUsPageLocators, NavigationMenuLocators
from Data.test_data import ContactUsData


class ContactUs():

    def __init__(self, browser):
        self.browser = browser
        self.menu_locator = NavigationMenuLocators
        self.locator = ContactUsPageLocators

    def check_type(self):
        self.browser.select_from_list(self.locator.LIST)

    def enter_description(self):
        data = ContactUsData.DESCRIPTION_FOR_CONTACT
        self.browser.send_keys_to_element(self.locator.DESCRIPTION, data)

    def get_text_from_list(self):
        a = self.browser.get_element_text(self.locator.TYPE)
        return a

    def get_text_from_result(self):
        res = self.browser.check_if_text_present(self.locator.MES, "Failed")
        return res

    def get_text_from_mes(self):
        res = self.browser.check_if_text_present(self.locator.REQUIRED, "Required")
        return res

    def get_text_from_desc(self):
        res = self.browser.check_if_text_present(self.locator.DESCRIPTION, "")
        return res







