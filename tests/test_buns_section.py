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

def test_buns_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    section_buns = driver.find_element(*SECTION_BUNS)
    driver.execute_script("arguments[0].scrollIntoView(true);", section_buns)
    driver.execute_script("arguments[0].click();", section_buns)

    active_buns_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SECTION_BUNS_1))

    assert active_buns_section.is_displayed()

