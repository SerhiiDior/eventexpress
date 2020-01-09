from Data.credentials import user,admin
import allure


@allure.feature('Search field')
@allure.story("Search EVENT")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_event(app):
    app.signin.enter_actor( admin['email'], admin['password'] )
    app.search.open_filter()
    app.search.enter_date_from('12/19/19')
    app.search.enter_date_to('12/20/19')
    app.search.click_button_search()
    assert (app.search.check_name_event() == "test")
