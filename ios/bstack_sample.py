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
        text_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
        )
        text_button.click()
        text_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
        )
        text_input.send_keys("hello@browserstack.com"+"\n")
        time.sleep(5)
        text_output = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
        )
        assert text_output!=None and text_output.text=="hello@browserstack.com"
