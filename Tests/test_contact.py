from utilities.testLogging import PyLogging
from Locators.locators import ContactUsPageLocators as locator
import allure


@allure.feature('Positive test')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://eventsexpress20200103054152.azurewebsites.net/home/events?page=1", name='Click me')
@allure.story('Test sending message to admin')
@allure.suite('Tests for "Contact us page"')
def test_contact_us(app, login, screenshot_on_failure):
    loger = PyLogging(__name__)
    loger.info("New test:")
    messages = ("Go to 'Contact us' page.", "Check type of a list",
                "Enter description", "Click on 'Submit' button", "Test Passed")
    messages_error = "Test Failed, message don't send to admin"

    with allure.step(messages[0]):
        app.navigation.click_on_contact_us()
        loger.info(messages[0])
    app.base.element_be_clickable(locator.SUBMIT)
    with allure.step(messages[1]):
        app.contact.check_type()
        loger.info(messages[1])
        app.contact.get_text_from_list()
    with allure.step(messages[2]):
        app.contact.enter_description()
        loger.info(messages[2])
    with allure.step(messages[3]):
        app.base.click_on_element(locator.SUBMIT)
        loger.info(messages[3])
    res = app.contact.get_text_from_result()
    if res == False:
        loger.error(messages_error)
        assert res, messages_error
    else:
        loger.info(messages[4])










