from Data.credentials import user,admin
import pytest
import allure
from Data.test_data import CategoriesPage

@allure.link("http://localhost:57690/admin/categories/", name='Click me')
@allure.feature('Login User')
@allure.story('Test creating category')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_category(app,login_admin,screenshot_on_failure):

    category_old = CategoriesPage.category_old
    with allure.step("Go to Categories page."):
        app.navigation.click_on_categories()
    with allure.step("Creating Category."):
        app.categories.add_category(category_old)
        assert (app.categories.check_category_added(category_old) == True), "Category was not created"

    #teatdown
    app.categories.delete_category(category_old)