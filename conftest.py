import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import spelly_mobile_test.utils.selene.patch_selector_strategy  # noqa
    import spelly_mobile_test.utils.selene.patch_element_mobile_commands  # noqa