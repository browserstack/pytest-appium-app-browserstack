from browserstack.local import Local
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('setWebdriver')
class TestSample:

    def test_example(self):
        search_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
            )

        search_element.click()
        search_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
            )
        search_input.send_keys("BrowserStack")
        time.sleep(5)
        search_results = self.driver.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView")
        
        assert len(search_results) > 0
