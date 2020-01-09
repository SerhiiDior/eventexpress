from Tests.test_init import TestInit
from Locators.locators import RegisterLocators




class TestRegister(TestInit):

    def setUp(self):
        super().setUp()
        self.locator_reg = RegisterLocators




    def test_register_user_clickable_clear(self):
        self.exec.signin.click_sign_in_up()
        self.exec.signin.click_on_register()
        self.exec.base.send_keys_to_element(self.locator_reg.EMAIL_SIGNIN, 'hello')
        self.assertTrue(self.exec.base.element_be_clickable(self.locator_reg.CLEAR), "element is not clickable")




