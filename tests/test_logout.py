import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_logout(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("natalya_goncharova_12@yandex.ru")

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("test123")

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*PROFILE_ELEMENT).click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON)
    )
    logout_button.click()

    time.sleep(2)

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    print("Current URL after login:", driver.current_url)