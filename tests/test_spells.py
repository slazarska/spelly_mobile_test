import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have, be
from selene.support.shared import browser


@allure.tag("mobile")
@allure.feature("Browserstack")
@allure.story("Mobile tests on Wikipedia with Browserstack")
def test_open_spell():
    with allure.step('Click on the search field'):
        browser.element((AppiumBy.ID, "header_text_view")).click()
    with allure.step('Search "The Last of Us"'):
        browser.element((AppiumBy.ID, "activity_selected_spell").should(be.visible))
        # browser.element((AppiumBy.ACCESSIBILITY_ID, "spell_type")).should(be.visible))
        # browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("The Last of Us")
    #with allure.step('Check the search result is not null'):
        #browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))