from typing import Tuple

from selenium.webdriver.common.by import By

LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

LOGIN_EMAIL_INPUT = (By.NAME, "name")

LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль")

LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

PROFILE_ELEMENT = (By.XPATH, "//p[text()='Личный Кабинет']")

LOGIN_SUBMIT_BUTTON_REGISTRATE = (By.XPATH, "//a[@href='/login' and text()='Войти']")

CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/' and contains(@class, 'AppHeader_header__link')]")

LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

SECTION_BUNS = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Булки']")

SECTION_BUNS_1 = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")

SECTION_SAUCE = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Соусы']")

SECTION_SAUCE_1 = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")

SECTION_FILLINGS = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']")

SECTION_FILLINGS_1 = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")