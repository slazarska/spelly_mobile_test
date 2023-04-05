import allure_commons
import pytest
from appium import webdriver
from selene import support
from selene.support.shared import browser

import config
from spelly_mobile_test import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    yield

    session_id = browser.driver.session_id

    if config.settings.run_on_browserstack:
        utils.attach.screenshot(name=f'Last screenshot_{session_id}')
        utils.attach.screen_xml_dump(name=f'XML_dump_{session_id}')

    browser.quit()

    if config.settings.run_on_browserstack:
        utils.attach.video_from_browserstack(session_id)
