from utilities.testLogging import PyLogging
from Locators.locators import ContactUsPageLocators as locator
import allure


@allure.suite('Tests for "Contact us page"')
@allure.feature("Message 'Required'")
@allure.link("https://eventsexpress20200103054152.azurewebsites.net/home/events?page=1", name='Click me')
@allure.story("Test appearance message 'Required'")
@allure.severity(allure.severity_level.CRITICAL)
def test_contact_us_negative(app, login, screenshot_on_failure):
    loger = PyLogging(__name__)
    loger.infos.append("New test:")
    messages = ("Go to 'Contact us' page.",
                "Check type of a list",
                "Click on description field",
                "Check if message show",
                "Test Passed")
    messages_error = "Test Failed, didn't show message 'Required'"

    with allure.step(messages[0]):
        app.navigation.click_on_contact_us()
        loger.info(messages[0])
    app.base.element_be_clickable(locator.SUBMIT)
    with allure.step(messages[1]):
        app.contact.check_type()
        loger.info(messages[1])
    with allure.step(messages[2]):
        app.base.click_on_element(locator.DESCRIPTION)
        loger.info(messages[2])
    with allure.step(messages[3]):
        app.navigation.click_on_contact_us()
        loger.info(messages[3])
    res = app.contact.get_text_from_mes()
    if res == False:
        loger.error(messages_error)
        # loger.sendreport()
        assert res, messages_error
    else:
        loger.info(messages[4])
        # loger.sendreport()



