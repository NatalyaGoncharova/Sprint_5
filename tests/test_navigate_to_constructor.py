from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *


def test_navigate_to_construction(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*PROFILE_ELEMENT).click()

    constructor_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)
    )
    constructor_button.click()

    assert driver.current_url == BASE_URL
    print("Current URL after login:", driver.current_url)