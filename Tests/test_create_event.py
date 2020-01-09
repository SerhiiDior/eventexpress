from Data.credentials import user,admin
from Data.test_data import CreateEventData
from Locators.locators import CreateEvent


event = CreateEventData
locator = CreateEvent


def test_create_event(app):
    app.signin.enter_actor( user['email'], user['password'] )
    app.navigation.click_on_profile( )
    app.prof_menu.click_on_add_event( )
    app.creat_event.upload_image( )
    app.creat_event.add_title( event.TITLE )
    text = event.DESCRIPTION['New Year']  # text add into description field for testing
    app.creat_event.add_desc( text )
    # text2 = 'hello'
    assert app.base.check_if_text_present( locator.DESC_TEXT, text )
    # self.exec.base.get_element_text(self.locator.DESC_TEXT)
    app.base.click_on_element( locator.CATEGORY )
    app.creat_event.add_category( locator.LST_CATEGORIES )
    app.base.click_action(0, 0)

    app.base.scroll_to_element( locator.COUNTRY_FIELD )

    app.base.click_on_element( locator.COUNTRY_FIELD )

    app.creat_event.select_country( locator.COUNTRY_FIELD )

    app.base.click_on_element( locator.CITY )
    app.creat_event.select_city(locator.CITY)

    # app.creat_event.press_button_save( )
    #
    # app.base.check_if_element_exists( locator.SUCCESS_MSG )
    # app.base.get_element_text( locator.SUCCESS_MSG )









