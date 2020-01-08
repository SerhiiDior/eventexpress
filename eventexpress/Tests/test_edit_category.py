from Data.credentials import user,admin
import pytest
import allure
from utilities.testLogging import TestLogging
from Data.test_data import CategoriesPage
@allure.link("http://localhost:57690/admin/categories/", name='Click me')
@allure.feature('Login User')
@allure.story('Test editing category')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_category(app,login_admin,screenshot_on_failure):
    category_old = CategoriesPage.category_old
    category_new = CategoriesPage.category_new
    loger=TestLogging(__name__)
    loger.infos.append("New test:")
    messages = ("Go to Categories page.",
                "Creating Category {}.".format(category_old),
                "Editing Category {} to {}".format(category_old,category_new))
    messages_error = ("Category {} was not created".format(category_old),
                      "Category {} was not edited to {}".format(category_old,category_new),
                      "Test Failed")
    with allure.step(messages[0]):
        loger.infos.append(messages[0])
        app.navigation.click_on_categories()
    with allure.step(messages[1]):
        loger.infos.append(messages[1])
        app.categories.add_category(category_old)
        if app.categories.check_category_added(category_old)==True:
            test1=True
        else:
            test1=False
            loger.errors.append(messages_error[0])
            loger.sendreport()
            assert test1 , messages_error[0]
    with allure.step(messages[2]):
        loger.infos.append(messages[2])
        app.categories.edit_category(category_old, category_new)
        if app.categories.check_category_added(category_old)==True:
            test2=True
        else:
            test2=False
            loger.errors.append(messages_error[1])
            loger.sendreport()
            assert test2, messages_error[1]


    if test1 and test2:
        test3=True
    else:
        test3=False
        loger.criticals.append(messages_error[2])
    loger.sendreport()
    app.categories.delete_category(category_new)
    assert test3, messages_error[2]

    #teardown
    app.categories.delete_category(category_new)

