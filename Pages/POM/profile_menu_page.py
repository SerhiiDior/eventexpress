from Locators.locators import ProfileMenuLocators


class ProfileMenu:
    '''Page object for profile page item at navigation menu'''

    def __init__(self, browser):
        self.browser = browser
        self.locator = ProfileMenuLocators

    def click_on_add_event(self):
        self.browser.click_on_element(self.locator.ADD_EVENT)

