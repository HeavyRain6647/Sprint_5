from selenium.webdriver.common.by import By

# Ссылки
LINK_REGISTER = (By.LINK_TEXT, "Зарегистрироваться")
LINK_PROFILE = (By.PARTIAL_LINK_TEXT, "Личный кабинет")
LINK_ALREADY_ACCOUNT = (By.LINK_TEXT, "Уже есть аккаунт?")
LINK_RECOVERY = (By.LINK_TEXT, "Восстановить пароль")
LINK_RETURN_TO_LOGIN = (By.LINK_TEXT, "Вернуться к форме входа")

# Поля ввода
INPUT_NAME = (By.NAME, "name")
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
PROFILE_NAME_INPUT = (By.NAME, "profile-name")
PROFILE_EMAIL_INPUT = (By.NAME, "profile-email")

# Кнопки
BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
BUTTON_MAIN_LOGIN = (By.XPATH, "//button[.//span[text()='Войти в аккаунт']]")
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
BUTTON_CONSTRUCTOR = (By.XPATH, "//a[text()='Конструктор']")
BUTTON_LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
PROFILE_SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
PROFILE_CANCEL_BUTTON = (By.XPATH, "//button[text()='Отменить']")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

# Разделы конструктора
SECTION_BUNS = (By.XPATH, "//div[text()='Булки']")
SECTION_SAUCES = (By.XPATH, "//div[text()='Соусы']")
SECTION_FILLINGS = (By.XPATH, "//div[text()='Начинки']")

# Прочие элементы
LOGO = (By.CSS_SELECTOR, "header [class*='logo']")
MENU_PROFILE = (By.PARTIAL_LINK_TEXT, "Профиль")
ERROR_INPUT = (By.CLASS_NAME, "input__error")
SUCCESS_REGISTRATION = (By.CLASS_NAME, "registration-success")
CARD_TITLE = (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']")
AVATAR_EDIT_BUTTON = (By.XPATH, "//button[@class='profile__edit-avatar']")
