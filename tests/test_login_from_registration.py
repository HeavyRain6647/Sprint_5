def test_login_from_registration(driver, wait, user_data):
    """Вход из формы регистрации (переход к форме входа)."""
    wait.until(EC.element_to_be_clickable
              ((By.LINK_TEXT, "Зарегистрироваться")).click()

    driver.find_element(By.LINK_TEXT, "Уже есть аккаунт?").click()

    driver.find_element(By.NAME, "email").send_keys(user_data["email"])
    driver.find_element(By.NAME, "password").send_keys(user_data["password"])
    wait.until(EC.element_to_be_clickable
              ((By.XPATH, "//button[text()='Войти']")).click()

    wait.until(EC.visibility_of_element_located
              ((By.PARTIAL_LINK_TEXT, "Профиль")))
    assert "Профиль" in driver.page_source
