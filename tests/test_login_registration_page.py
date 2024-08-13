from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_from_registration_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*LOGIN_SUBMIT_BUTTON_REGISTRATE).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("natalya_goncharova_12@yandex.ru")

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("test123")

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be('https://stellarburgers.nomoreparties.site/')
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    print("Current URL after login:", driver.current_url)