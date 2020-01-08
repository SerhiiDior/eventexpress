from Data.credentials import user,admin
from Locators.locators import ContactUsPageLocators as locator
import allure


@allure.feature("Message 'Required'")
@allure.severity(allure.severity_level.CRITICAL)
def test_contact_us_clear(app, screenshot_on_failure):
    with allure.step("Login as user"):
        app.signin.enter_actor(user['email'],user['password'])

    with allure.step("Navigation 'Contact us'"):
        app.navigation.click_on_contact_us()
    app.base.element_be_clickable(locator.SUBMIT)
    with allure.step("Check type of a list"):
        app.contact.check_type()
    with allure.step("Get text from list"):
        app.contact.get_text_from_list()
    with allure.step("Enter description"):
        app.contact.enter_description()
    with allure.step("Click on 'Clear' button"):
        app.base.click_on_element(locator.CLEAR)
    assert(app.base.get_element_text(locator.DESCRIPTION) == "")








