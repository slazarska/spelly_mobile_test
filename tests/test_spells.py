import allure
from allure_commons.types import Severity
from spelly_mobile_test.model import app


@allure.tag('ui', 'mobile')
@allure.label('owner', 'slazarska')
@allure.feature('Spells')
class TestsSpells:

    @allure.severity(Severity.BLOCKER)
    @allure.story('Main functionality')
    @allure.title('Open spells screen')
    def test_open_spell(self):
        app.main_screen.check_main_screen_is_opened()
        app.main_screen.open_spells_screen()
        app.spell_screen.check_spells_screen_is_opened()

    @allure.severity(Severity.CRITICAL)
    @allure.story('Main functionality')
    @allure.title('Return to the main page from the spells page')
    def test_return_to_main_screen(self):
        app.main_screen.open_spells_screen()
        app.spell_screen.go_back_to_main_screen()
        app.main_screen.check_main_screen_is_opened()

    @allure.severity(Severity.NORMAL)
    @allure.story('Elements on the spells page')
    @allure.title('Check the spells name')
    def test_spells_name(self):
        app.main_screen.open_spells_screen()
        app.spell_screen.check_spells_name('Alohomora')

    @allure.severity(Severity.NORMAL)
    @allure.story('Elements on the spells page')
    @allure.title('Check the main attributes of spell on the spells page')
    def test_spells_description(self):
        app.main_screen.open_spells_screen()
        app.spell_screen.check_spells_action()
        app.spell_screen.check_spells_type()
        app.spell_screen.check_spells_quote()

    @allure.severity(Severity.NORMAL)
    @allure.story('Favorites')
    @allure.title('Check the spell can be added to the list of favorite spells')
    def test_add_spell_to_favorites(self):
        app.main_screen.tap_favorite_icon()
        app.main_screen.click_on_filters()
        app.main_screen.choose_favorites_filter()
        app.main_screen.choose_favorites_spells()
        app.main_screen.check_favorites_list()
