def test_registration_short_password(driver, wait, user_data):
    """Ошибка при пароле < 6 символов."""
    wait.until(EC.element_to_be_clickable
              ((By.LINK_TEXT, "Зарегистрироваться")).click()

    driver.find_element(By.NAME, "name").send_keys("Тест Пользователь")
    driver.find_element(By.NAME, "email").send_keys(user_data["email"])
    driver.find_element(By.NAME, "password").send_keys("12345")  # 5 символов


    wait.until(EC.element_to_be_clickable
              ((By.XPATH, "//button[text()='Зарегистрироваться']")).click()


    error_msg = wait.until(EC.visibility_of_element_located
                     ((By.CLASS_NAME, "input__error")))
    assert "Некорректный пароль" in error_msg.text
