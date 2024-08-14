from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *

def test_logout(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    driver.find_element(*PROFILE_ELEMENT).click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON)
    )
    logout_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )

    assert driver.current_url == LOGIN_URL
    print("Current URL after login:", driver.current_url)