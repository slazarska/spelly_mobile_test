import allure
from selene import have, be
from selene.support.shared import browser


class SpellScreen:
    @allure.step
    def check_spells_page_is_opened(self):
        browser.element('#activity_selected_spell').should(be.enabled)
        return self

    @allure.step
    def check_spells_name_on_the_spell_screen(self, spell_name='text'):
        browser.element('#spell_name').should(have.text(spell_name))
        return self

    @allure.step
    def check_action_on_the_spell_screen(self):
        browser.element('#spell_action').should(be.enabled)
        return self

    @allure.step
    def check_spells_type_on_the_spell_screen(self):
        browser.element('#spell_type').should(be.enabled)
        return self

    @allure.step
    def check_quote_on_the_spell_screen(self):
        browser.element('#spell_quote').should(be.enabled)
        return self

    @allure.step
    def go_back_to_main_screen(self):
        browser.driver.back()
        return self
