import allure
from selene import have, be
from selene.support.shared import browser

"""
class FullscreenPopup:
    @step
    def should_be_visible(self):
        browser.element('#tvFullscreen').should(be.visible)
        return self

    @step
    def should_have_text(self, value):
        browser.element('#tvFullscreen').should(have.exact_text(value))
        return self

    @step
    def tap_close_button(self):
        browser.element('#closeButton').tap()
        return self
"""


class MainScreen:

    @allure.step
    def should_be_visible_translate_site_button(self):
        browser.element('#btnTrUrl').should(be.visible)
        return self

    @allure.step
    def tap_cross_icon(self):
        browser.element('#clearButton').tap()
        return self

    @allure.step
    def tap_switch_language(self):
        browser.element('#ib_translate_switch_langs').tap()
        return self

    # fullscreen_popup = FullscreenPopup()
