from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    NAME_INPUT = By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]"
    EMAIL_INPUT = By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]"
    PASSWORD_INPUT = (By.NAME, "Пароль")
    REG_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"] #кнопка "Зарегистрироваться"

    EMAIL = (By.NAME, "name") #поле ввода почты зарегистрированного пользователя
    PASSWORD = (By.NAME, "Пароль") #поле ввода пароля зарегистрированного пользователя

    # Локаторы для входа
    ENT_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнопка «Войти»
    PERSONAL_ACC = (By.XPATH, "//p[text()='Личный Кабинет']") #переход в раздел Личный кабинет

