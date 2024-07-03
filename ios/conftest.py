import pytest
from appium import webdriver

@pytest.fixture(scope='function')
def setWebdriver(request, session_capabilities):
    remoteURL = "https://hub.browserstack.com/wd/hub"
    driver = webdriver.Remote(remoteURL, session_capabilities)
    request.instance.driver = driver
    request.node._driver = driver
    yield driver
    driver.quit()
