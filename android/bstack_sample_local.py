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
        test_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.example.android.basicnetworking:id/test_action"))
            )

        test_button.click()

        time.sleep(5)
        
        test_element = None
        search_results = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        print(len(search_results))
        for result in search_results:
            if "Up and running" in result.text:
                test_element = result

        assert test_element is not None
