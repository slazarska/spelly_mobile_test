import allure
from selene import be
from selene.support.shared import browser


class MainScreen:
    @allure.step
    def open_spells_screen(self):
        browser.with_(timeout=10).element('#header_text_view').tap()
        return self

    @allure.step
    def check_return_from_spells_screen_on_main_screen(self):
        browser.element('#activity_selected_spell').should(not be.existing)
        return self
