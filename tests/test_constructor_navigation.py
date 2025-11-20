import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import CONSTRUCTOR_PAGE
from locators import (
    LOGO,
    SECTION_BUNS,
    SECTION_SAUCES,
    SECTION_FILLINGS
)


class TestConstructorNavigation:
    """Тесты для проверки переключения между табами в конструкторе."""


    @pytest.mark.parametrize(
    ("tab_locator, section_name"), [
        (SECTION_BUNS, "Булки"),
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ])
    def test_constructor_tab_navigation(self, driver, wait, login, tab_locator, section_name):
        """
        Проверяет переключение между табами в конструкторе.
        Использует параметризацию для атомарного тестирования каждого таба.
        """
        # 1. Переход на страницу конструктора
        driver.get(CONSTRUCTOR_PAGE)


        # 2. Ожидание загрузки и видимости логотипа
        wait.until(EC.visibility_of_element_located(LOGO))


        # 3. Клик по табу
        tab_element = wait.until(EC.element_to_be_clickable(tab_locator))
        tab_element.click()

        # 4. Проверка активности таба (класс 'active')
        assert "active" in tab_element.get_attribute("class"), (
            f"Таб '{section_name}' не стал активным"
        )

        # 5. Проверка видимости контента таба
        content_locator = (By.XPATH, f"//div[text()='{section_name}']")
        wait.until(EC.visibility_of_element_located(content_locator))

