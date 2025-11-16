def test_registration_success(driver, wait, user_data):
    """Успешная регистрация с корректными данными."""
    wait.until(EC.element_to_be_clickable
              ((By.LINK_TEXT, "Зарегистрироваться")).click()


    driver.find_element(By.NAME, "name").send_keys("Тест Пользователь")
    driver.find_element(By.NAME, "email").send_keys(user_data["email"])
    driver.find_element(By.NAME, "password").send_keys(user_data["password"])


    wait.until(EC.element_to_be_clickable
              ((By.XPATH, "//button[text()='Зарегистрироваться']")).click()


    wait.until(EC.visibility_of_element_located
              ((By.PARTIAL_LINK_TEXT, "Профиль")))
    assert "Профиль" in driver.page_source
