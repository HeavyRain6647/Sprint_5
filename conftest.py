import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL, LOGIN_PAGE
from data import TEST_USER
from locators import (
    BUTTON_MAIN_LOGIN,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE,
    BUTTON_LOGOUT,
)

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def login(driver, wait):
    """Выполняет авторизацию с использованием данных из data.py."""
    if driver.current_url != LOGIN_PAGE:
        driver.get(LOGIN_PAGE)

    wait.until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()

    email_input = wait.until(EC.visibility_of_element_located(INPUT_EMAIL))
    email_input.clear()
    email_input.send_keys(TEST_USER["email"])


    password_input = driver.find_element(*INPUT_PASSWORD)
    password_input.clear()
    password_input.send_keys(TEST_USER["password"])


    login_button = wait.until(EC.element_to_be_clickable(BUTTON_LOGIN))
    login_button.click()

    wait.until(EC.url_contains("/profile"))
    wait.until(EC.visibility_of_element_located(MENU_PROFILE))

@pytest.fixture
def logout(driver, wait):
    """Выходит из аккаунта после теста."""
    try:
        logout_button = wait.until(EC.element_to_be_clickable(BUTTON_LOGOUT))
        logout_button.click()
        wait.until(EC.url_to_be(LOGIN_PAGE))
    except Exception as e:
        print(f"Ошибка при выходе из аккаунта: {e}")
