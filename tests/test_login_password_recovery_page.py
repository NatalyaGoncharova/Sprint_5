from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *


def test_login_from_password_recovery_page(driver):
    driver.get(RESSET_URL)

    driver.find_element(*LOGIN_SUBMIT_BUTTON_REGISTRATE).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)

    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    assert driver.current_url == BASE_URL
    print("Current URL after login:", driver.current_url)