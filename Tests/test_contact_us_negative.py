from Data.credentials import user,admin
from Locators.locators import ContactUsPageLocators as locator
import allure


@allure.feature("Message 'Required'")
def test_contact_us_negative(app, screenshot_on_failure):
    with allure.step("Login"):
        app.signin.enter_actor(user['email'],user['password'])

    with allure.step("Navigation 'Contact us'"):
        app.navigation.click_on_contact_us()
    app.base.element_be_clickable(locator.SUBMIT)
    app.base.click_on_element(locator.DESCRIPTION)
    app.navigation.click_on_contact_us()
    with allure.step("Message 'Required'"):
        mes = "Required"
        assert (app.base.get_element_text(locator.REQUIRED) == mes)



