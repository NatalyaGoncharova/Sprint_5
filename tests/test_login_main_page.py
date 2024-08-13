import pytest
from selenium import webdriver
from locators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("natalya_goncharova_12@yandex.ru")

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("test123")

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*PROFILE_ELEMENT).click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
    print("Current URL after login:", driver.current_url)