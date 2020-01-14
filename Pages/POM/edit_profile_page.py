from Locators.locators import EditYourProfile, NavigationMenuLocators
from Data.test_data import EditProfileData

class EditProfile():


    def __init__(self, browser):
        self.browser = browser
        self.menu_locator = NavigationMenuLocators
        self.locator = EditYourProfile
        self.data = EditProfileData

