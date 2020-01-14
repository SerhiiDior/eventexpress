import pytest
from Data.test_data import ProfileMenuPageHeaderInfo as data
from Locators.locators import ProfileMenuPageHeaderInfoLocators as locator


@pytest.mark.parametrize("userinfo_input", ['User Name:',
                                            'UserTest',
                                            'Age:',
                                            '19',
                                            'Gender:',
                                            'Other',
                                            'Email:',
                                            'user@gmail.com',
                                            'Interests:'
                                            ])
def test_event_menu_header_info_text(app, login, userinfo_input):
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(userinfo_input)
    userinfo_expected_value = userinfo_input
    assert actual_text == userinfo_expected_value, f"Text of {userinfo_input} item differs. The expected one is {userinfo_expected_value} instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")

@pytest.mark.skip(reason='Postponded for USER_INTERESTS_DATA actualyzing')
def test_event_menu_header_info_text_interests(app, login, userinfo_input=data.USER_INTERESTS_DATA):
    '''Check the Interests list'''
    app.navigation.click_on_profile()
    actual_text = app.event_menu.get_text(locator)
    userinfo_expected_value = data.USER_INTERESTS_DATA
    assert actual_text in userinfo_expected_value, f"Text of {userinfo_input} item differs. The expected one is {userinfo_expected_value} instead {actual_text} is displayed"
    print(f"Text of {userinfo_input} is in the tab {userinfo_expected_value}")
