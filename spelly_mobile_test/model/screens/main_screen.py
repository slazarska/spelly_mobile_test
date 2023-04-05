import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, have
from selene.support.shared import browser


class MainScreen:
    @allure.step('Open spells page')
    def open_spells_screen(self):
        browser.with_(timeout=10).element((AppiumBy.ID, "header_text_view")).should(be.visible).tap()
        return self

    @allure.step('Check the main page is opened')
    def check_main_screen_is_opened(self):
        browser.element((AppiumBy.ID, "activity_main")).should(be.enabled)
        return self

    @allure.step('Add the spell to favorites')
    def tap_favorite_icon(self):
        browser.element((AppiumBy.ID, "fav_image")).tap()
        return self

    @allure.step('Expand filters')
    def click_on_filters(self):
        browser.element((AppiumBy.ID, "filter")).tap()
        return self

    @allure.step('Choose the filter for the favorites/non favorites spells')
    def choose_favorites_filter(self):
        browser.all((AppiumBy.ID, "title")).element(1).tap()
        return self

    @allure.step('Choose the list of the favorites spells')
    def choose_favorites_spells(self):
        browser.all((AppiumBy.ID, "title")).element(0).tap()
        return self

    @allure.step('Check the list of the favorites spells is not empty')
    def check_favorites_list(self):
        browser.all((AppiumBy.ID, "list_view")).matching(have.size_greater_than(0))
        return self
