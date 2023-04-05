import allure
from selene import have, be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


class SpellScreen:
    @allure.step('Check the spells page is opened')
    def check_spells_screen_is_opened(self):
        browser.element((AppiumBy.ID, "activity_selected_spell")).should(be.enabled)
        return self

    @allure.step('Check the spells name on the spells page')
    def check_spells_name(self, spell_name='text'):
        browser.element((AppiumBy.ID, "spell_name")).should(have.text(spell_name))
        return self

    @allure.step('Check the spells page contains an action section')
    def check_spells_action(self):
        browser.element((AppiumBy.ID, "spell_action")).should(be.enabled)
        return self

    @allure.step('Check the spells page contains a spells type')
    def check_spells_type(self):
        browser.element((AppiumBy.ID, 'spell_type')).should(be.enabled)
        return self

    @allure.step('Check the spells page contains a quote section')
    def check_spells_quote(self):
        browser.element((AppiumBy.ID, 'spell_quote')).should(be.enabled)
        return self

    @allure.step('Return to the main page')
    def go_back_to_main_screen(self):
        browser.driver.back()
        return self
