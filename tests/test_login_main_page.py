from locators import *
from data import *


def test_login_from_main_page(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*PROFILE_ELEMENT).click()

    assert driver.current_url == ACCOUNT_URL
    print("Current URL after login:", driver.current_url)