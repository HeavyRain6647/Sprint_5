def test_logout(driver, wait, login):
    logout(driver, wait)
    assert "/login" in driver.current_url
