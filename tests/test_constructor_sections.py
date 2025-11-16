def test_constructor_sections(driver, wait, login):
    """
    Проверяет работу вкладок в разделе «Конструктор»:
    - «Булки»
    - «Соусы»
    - «Начинки»
    """
    # 1. Переход в конструктор
    wait.until(EC.element_to_be_clickable(
               (By.XPATH, "//a[text()='Конструктор']")).click()
    wait.until(EC.url_contains("/constructor"))

    # 2. Проверка вкладки «Булки»
    buns_tab = wait.until(EC.element_to_be_clickable(
                       (By.XPATH, "//div[text()='Булки']"))
    buns_tab.click()
    
    # Проверка активности вкладки (например, наличие класса 'active')
    assert "active" in buns_tab.get_attribute("class")
    
    # Дополнительно: проверяем видимость элементов раздела «Булки»
    wait.until(EC.visibility_of_element_located(
               (By.XPATH, "//div[@class='places__item' and .//div[text()='Булка']]"))

    # 3. Проверка вкладки «Соусы»
    sauces_tab = wait.until(EC.element_to_be_clickable(
                 (By.XPATH, "//div[text()='Соусы']"))
    sauces_tab.click()
    
    assert "active" in sauces_tab.get_attribute("class")
    wait.until(EC.visibility_of_element_located(
               (By.XPATH, "//div[@class='places__item' and .//div[text()='Соус']]"))

    # 4. Проверка вкладки «Начинки»
    fillings_tab = wait.until(EC.element_to_be_clickable(
                  (By.XPATH, "//div[text()='Начинки']"))
    fillings_tab.click()
    
    assert "active" in fillings_tab.get_attribute("class")
    wait.until(EC.visibility_of_element_located(
               (By.XPATH, "//div[@class='places__item' and .//div[text()='Начинка']]"))
