import allure
from allure_commons.types import Severity
from spelly_mobile_test.model import app


@allure.tag("mobile")
@allure.label('owner', 'slazarska')
@allure.feature(' ')
@allure.story(' ')
class TestsSpells:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Open spells screen')
    def test_open_spell(self):
        app.main_screen.open_spells_screen()
        app.spell_screen.check_spells_page_is_opened()

    @allure.severity(Severity.CRITICAL)
    @allure.title(' ')
    def test_go_back(self):
        app.main_screen.open_spells_screen()
        app.spell_screen.go_back_to_main_screen()

    @allure.severity(Severity.NORMAL)
    @allure.title(' ')
    def test_check_spell_name(self):
        app.main_screen.open_spells_screen()
        app.spell_screen.check_spells_name_on_the_spell_screen('Alohomora')

    @allure.severity(Severity.NORMAL)
    @allure.title(' ')
    def test_spell_has_action(self):
        app.spell_screen.check_action_on_the_spell_screen()
        app.spell_screen.check_spells_type_on_the_spell_screen()
        app.spell_screen.check_quote_on_the_spell_screen()
