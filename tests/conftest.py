
import pytest
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser
from appium import webdriver
from utils.attach_video import attach


@pytest.fixture(scope='function', autouse=True)
def driver_manager():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Samsung Galaxy S10",
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": "olga_rubUyz",
            "accessKey": "tNKt2nEjirtszq9qdgi2"
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    #attach(browser)
    browser.quit()
