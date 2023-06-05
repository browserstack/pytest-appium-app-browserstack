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

        def existence_lambda(s):
            result = s.find_element(AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal").get_attribute("value")
            return result and len(result) > 0

        test_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "TestBrowserStackLocal"))
        )
        test_button.click()
        WebDriverWait(self.driver, 30).until(existence_lambda)

        time.sleep(5)
        result_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ResultBrowserStackLocal")
        result_string = result_element.text.lower()
        assert result_string.__contains__("up and running")
        
        