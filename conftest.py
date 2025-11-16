import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver():
    """Инициализирует браузер и закрывает его после всех тестов."""
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    """Возвращает объект WebDriverWait с таймаутом 10 сек."""
    return WebDriverWait(driver, 10)

@pytest.fixture
def user_data():
    """Тестовые данные для регистрации/авторизации."""
    return {
        "email": "magomed_khusainov_34_777@yandex.ru",
        "password": "qwerty123"
    }

@pytest.fixture
def login(driver, wait, user_data):
    """Выполняет вход в аккаунт перед тестом."""
    wait.until(EC.element_to_be_clickable(
              ((By.XPATH, "//button[.//span[text()='Войти в аккаунт']]"))).click()
    
    driver.find_element(By.NAME, "email").send_keys(user_data["email"])
    driver.find_element(By.NAME, "password").send_keys(user_data["password"])
    wait.until(EC.element_to_be_clickable
              ((By.XPATH, "//button[text()='Войти']"))).click()
    wait.until(EC.visibility_of_element_located
              ((By.PARTIAL_LINK_TEXT, "Профиль")))


@pytest.fixture
def logout(driver, wait):
    """Выходит из аккаунта после теста."""
    wait.until(EC.element_to_be_clickable
              ((By.XPATH, "//button[text()='Выйти']"))).click()
    wait.until(EC.url_contains("/login"))
