import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have
from selene.support.shared import browser


@allure.tag("mobile")
@allure.feature("Browserstack")
@allure.story("Mobile tests on Wikipedia with Browserstack")
def test_search_browserstack_on_wiki():
    with allure.step('Click on the search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step('Enter "Browserstack"'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    with allure.step('Check the search result'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


@allure.tag("mobile")
@allure.feature("Browserstack")
@allure.story("Mobile tests on Wikipedia with Browserstack")
def test_search_python_on_wiki():
    with allure.step('Click on the search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step('Search "The Last of Us"'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("The Last of Us")
    with allure.step('Check the search result is not null'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))