from Locators.locators import CreateEvent
from Data.test_data import CreateEventData
from selenium.webdriver.common.keys import Keys

import random



class CreateEvents():

    def __init__(self,browser):
        self.browser = browser
        self.locator = CreateEvent
        self.data = CreateEventData


    def add_title(self,data):
        self.browser.clean_element( self.locator.EVENT_TITLE)
        self.browser.send_keys_to_element(self.locator.EVENT_TITLE,data)

    def upload_image(self):
        self.browser.upload_file(self.data.IMAGE, self.locator.UPLOAD_PICTURE)

    def add_desc(self,data):
        self.browser.clean_element( self.locator.DESC_TEXT )
        self.browser.send_keys_to_element(self.locator.DESC_TEXT, data)

    # n - it's number of categories
    # will be add. In test we must import module random
    #adding will start after click on field category
    def add_category(self, *locator_cat):
        n = random.randint(1,4)
        while n > 0:
            lst = self.browser.get_list_element( "innerHTML", *locator_cat )
            print(lst)
            lst = random.choice(lst)
            self.browser.send_keys_to_element(self.locator.CATEGORY, lst)
            self.browser.send_keys_to_element( self.locator.CATEGORY, Keys.ENTER)
            n -= 1

    def select_country(self, *locator):
        country = self.browser.select_from_list(self.locator.COUNTRY)
        confirm = self.browser.send_keys_to_element(*locator, country)
        return confirm

    def select_city(self, *locator):
        city = self.browser.select_from_list( self.locator.CITY )
        confirm = self.browser.send_keys_to_element( *locator, city)
        return confirm

    def press_button_save(self):
        self.browser.click_on_element(self.locator.SAVE)








        # num_of_categories = random.randint(1, n)
        # category.send_keys( random.choice( lst_li ) )
        # category.send_keys( Keys.ENTER )
        # num_of_categories -= 1


