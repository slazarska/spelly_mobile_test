import allure
import allure_commons
import pytest
import config
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selene.support.shared import browser
from selene import support
from appium import webdriver
from spelly_mobile_test import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with allure.step('Set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=config.settings.driver_options
        )

    yield

    session_id = browser.driver.session_id

    if config.settings.run_on_browserstack:
        utils.attach.screenshot(name=f'Last screenshot_{session_id}')
        utils.attach.screen_xml_dump(name=f'XML_dump_{session_id}')

    with allure.step('Close app session'):
        browser.quit()

    if config.settings.run_on_browserstack:
        utils.attach.video_from_browserstack(session_id)
