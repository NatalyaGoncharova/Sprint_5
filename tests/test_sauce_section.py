import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_sause_section_visibitity(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    section_sauce = driver.find_element(*SECTION_SAUCE)
    driver.execute_script("arguments[0].scrollIntoView(true);", section_sauce)
    driver.execute_script("arguments[0].click();", section_sauce)

    active_sauce_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SECTION_SAUCE_1))

    assert active_sauce_section.is_displayed()

