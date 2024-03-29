# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestregistrasi:
    def setup_method(self, method):
        self.driver = webdriver.Remote(
            command_executor="https://www.blibli.com/register?redirect=%2F",
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testregistrasi(self):
        self.driver.get("https://www.blibli.com/")
        self.driver.set_window_size(1440, 804)
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn__login")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".btn__register").click()
        self.driver.execute_script("window.scrollTo(0,104)")
        self.driver.find_element(
            By.CSS_SELECTOR, "#gdn-register-form > .b-clearable > label"
        ).click()
        self.driver.find_element(By.ID, "bli-input-2k9oi3i5").click()
        self.driver.find_element(By.ID, "bli-input-2k9oi3i5").send_keys("rosalinda")
        self.driver.find_element(By.ID, "gdn-register-form").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form__username label").click()
        self.driver.find_element(By.ID, "bli-input-ex9gk92y").send_keys(
            "rosalinda33333@gmailcom"
        )
        self.driver.find_element(By.ID, "bli-input-8606da68m").click()
        self.driver.find_element(By.ID, "bli-input-8606da68m").send_keys("asdsadasdasd")
        self.driver.find_element(By.CSS_SELECTOR, ".blu-checkbox > label").click()
        self.driver.find_element(By.CSS_SELECTOR, "button > svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".b-full-width").click()
