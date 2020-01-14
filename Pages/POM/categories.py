from Locators.locators import CategoriesLocators
from Locators.locators import NavigationMenuLocators
from selenium.webdriver.common.keys import Keys
import time



class Categories():

    def __init__(self, browser):
        self.browser = browser
        self.locator_categories = CategoriesLocators
        self.locator_nav = NavigationMenuLocators


    def click_on_categories(self):
        self.browser.click_on_element(self.locator_nav.CATEGORIES)

    def add_category(self,category):
        self.browser.click_on_element(self.locator_categories.ADD_CATEGORY_BUTTON)
        self.browser.send_keys_to_element(self.locator_categories.ADD_CATEGORY_FIELD,category)
        self.browser.click_on_element(self.locator_categories.ADD_CATEGORY_CHECK)
    
    def delete_category(self,category):
        #self.browser.find_element(*self.locator_categories.CAT)
        time.sleep(2)
        lenth=len(self.browser.find_elements(*self.locator_categories.CATEGORIES))+1
        print("\nDelete\nLenth=",lenth)
        for i in range(3,lenth):
            print("{}".format(i))
            print(self.browser.find_element_by_xpath("//tr["+str(i)+"]/td[1]").text)
            if self.browser.find_element_by_xpath("//tr["+str(i)+"]/td[1]").text==category:
                self.browser.find_element_by_xpath("//*[@id='main']/div/table/tbody/tr["+str(i)+"]/td[5]").click()
    
    def edit_category(self,category_old,category_new):
        time.sleep(2)
        lenth = len(self.browser.find_elements(*self.locator_categories.CATEGORIES)) + 1;
        print("\nEdit\nLenth=", lenth)
        for i in range(3, lenth):
            print("{}".format(i))
            print(self.browser.find_element_by_xpath("//tr[" + str(i) + "]/td[1]").text)
            if self.browser.find_element_by_xpath("//tr[" + str(i) + "]/td[1]").text == category_old:
                self.browser.find_element_by_xpath("//*[@id='main']/div/table/tbody/tr[" + str(i) + "]/td[4]").click()
                self.browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/table/tbody/tr[" + str(i) + "]/td[1]/form/div/div/div/input").clear()
                self.browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/table/tbody/tr[" + str(i) + "]/td[1]/form/div/div/div/input").send_keys(category_new)
                self.browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/table/tbody/tr[" + str(i) + "]/td[1]/form/div/div/div/input").send_keys(Keys.ENTER)
    def check_warning(self):
        if self.browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table/tbody/tr[8]/td[1]/form/div/div[2]').text=='The same category is already exist in database':
            w=self.browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/table/tbody/tr[8]/td[1]/form/div/div[2]').text
            return w

    def check_category_added(self,category):
        time.sleep(2)
        #self.browser.find_element(*self.locator_categories.CAT)
        #lenth=len(self.browser.find_element_by_tag("tr"))+1;
        lenth=len(self.browser.find_elements(*self.locator_categories.CATEGORIES))+1
        print("\nCheck\nLenth=",lenth)
        for i in range(3,lenth):
            print("{}".format(i))
            print(self.browser.find_element_by_xpath("//tr["+str(i)+"]/td[1]").text)
            if self.browser.find_element_by_xpath("//tr["+str(i)+"]/td[1]").text==category:
                return True
    def check_category_deleted(self,category):
        return False if self.check_category_added(category) else True
