import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_fillings_section_visibitity(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    section_fillings = driver.find_element(*SECTION_FILLINGS)
    driver.execute_script("arguments[0].scrollIntoView(true);", section_fillings)
    driver.execute_script("arguments[0].click();", section_fillings)

    active_fillings_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SECTION_FILLINGS_1))

    assert active_fillings_section.is_displayed()

