import pytest
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators


@pytest.mark.usefixtures("driver")
class TestGoogleSearch:
    
  def test_positiv_new_registration(self, driver):
    unique_email = f"user{random.randint(1, 9999)}@test.com"
    self.driver.get("https://qa-desk.stand.praktikum-services.ru")

    self.wait.until(EC.element_to_be_clickable(BaseLocators.BUTTON_LOGIN_REGISTRATION)).click()
    self.wait.until(EC.element_to_be_clickable(BaseLocators.BUTTON_NO_ACCOUNT)).click()

    self.driver.find_element(*BaseLocators.BUTTON_ENTER_EMAIL).send_keys(unique_email)
    self.driver.find_element(*BaseLocators.BUTTON_ENTER_PASSWORD).send_keys("Pass12345")
    self.driver.find_element(*BaseLocators.BUTTON_REPEAT_PASSWORD).send_keys("Pass12345")
    self.driver.find_element(*BaseLocators.BUTTON_CREATE_ACCONT).click()

    self.wait.until(EC.url_contains("registration"))

    assert "registration" in self.driver.current_url, "URL после регистрации не совпадает"

    user_name_element = self.wait.until(EC.visibility_of_element_located(BaseLocators.USER_PROFILE))
    avatar_button = self.wait.until(EC.element_to_be_clickable(BaseLocators.AVATAR))

    assert user_name_element.text == "User.", "Плашка 'User.' не отображается"
    assert avatar_button.is_displayed(), "Аватар не отображается"

    assert user_name_element.text == "User.", "Плашка 'User.' не отображается"
    assert avatar_button.is_displayed(), "Аватар не отображается"

