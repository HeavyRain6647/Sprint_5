import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import CONSTRUCTOR_PAGE
from locators import LOGO, SECTION_BUNS, SECTION_SAUCES, SECTION_FILLINGS
from selenium.webdriver.common.by import By

class TestConstructorSections:
    """Тесты для проверки секций (табов) в конструкторе."""

    @pytest.mark.parametrize(
    ("section_locator, section_name"), [
        (SECTION_BUNS, "Булки"),
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ])
    def test_section_navigation(self, driver, wait, login, section_locator, section_name):
        """Проверяет переключение между секциями конструктора."""
        driver.get(CONSTRUCTOR_PAGE)
        wait.until(EC.visibility_of_element_located(LOGO))

        section_tab = wait.until(EC.element_to_be_clickable(section_locator))
        section_tab.click()

        assert "active" in section_tab.get_attribute("class"), (
            f"Вкладка '{section_name}' не стала активной"
        )

        content_locator = (By.XPATH, f".//div[text()='{section_name}']")
        wait.until(EC.visibility_of_element_located(content_locator))
