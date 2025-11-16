def test_constructor_navigation(driver, wait, login):
    wait.until(EC.element_to_be_clickable
              ((By.XPATH, "//a[text()='Конструктор']")).click()
    assert "/constructor" in driver.current_url
