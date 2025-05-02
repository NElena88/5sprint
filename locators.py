from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    NAME_INPUT = By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]"
    EMAIL_INPUT = By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]"
    PASSWORD_INPUT = (By.NAME, "Пароль")
    REG_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"] #кнопка "Зарегистрироваться"

    EMAIL = (By.NAME, "name") #поле ввода почты зарегистрированного пользователя
    PASSWORD = (By.NAME, "Пароль") #поле ввода пароля зарегистрированного пользователя
    LINK_REG = (By.CSS_SELECTOR, ".Auth_link__1fOlj") # ссылка на регистрацию из формы Вход в личный кабинет

    # Локаторы для входа
    ENT_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнопка «Войти»
    PERSONAL_ACC = (By.XPATH, "//p[text()='Личный Кабинет']") #переход в раздел Личный кабинет
    ERR_PASSWORD = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")
    LOGINACC_BUTT = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка Войти в аккаунт на главной странице
    ENTRANCE = (By.XPATH, "//h2[text()='Вход']") # заголовок формы ввода логина/пароля Вход
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # ссылка на форму ввода логина/пароля Войти
    FORGOT_PASSW = (By.XPATH, "//a[text()='Восстановить пароль']") # ссылка на форму восстановления пароля
    RECOVER_PASSW = (By.XPATH, "//button[text()='Восстановить']") # кнопка Восставить пароль
    PROFILE = (By.CSS_SELECTOR, "a[href='/account/profile']") # активная ссылка Профиль
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # активная ссылка Конструктор
    HEAD_CONSTRUC = (By.CSS_SELECTOR, "h1.text_type_main-large.mb-5.mt-10") # заголовок конструктора Соберите бургер
    LOGO_LINK = (By.CSS_SELECTOR, "a[href='/']") # активная ссылка на конструктор через логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка Выход для выхода из аккаунта

    # Локаторы для конструктора
    SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']") # заголовок вкладки Соусы
    SECTION_TOPPIN = (By.XPATH, "//span[text()='Начинки']") # заголовок вкладки Начинки
    SECTION_ROLLS = (By.XPATH, "//span[text()='Булки']") # заголовок вкладки Булки
    HEADER_SAUC = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span") # заголовок раздела Соусы
    HEADER_TOPPIN = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span") # заголовок раздела Начинки
    HEADER_ROLLS = (By.XPATH, "//h2[text()='Булки']") # заголовок раздела Булки