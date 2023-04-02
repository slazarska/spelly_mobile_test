import allure
from selene import be
from selene.support.shared import browser
from spelly_mobile_test.model.main_screen import MainScreen

main_screen = MainScreen()


@allure.step
def open_app():
    if browser.element('#design_bottom_sheet').matching(be.visible):
        browser.element('.android.widget.Button').tap()
