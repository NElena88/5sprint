
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from curl import *
from helpers import generate_registration_account
from locators import Locators


class TestPersonalAccount:

    def test_successful_registration(self, driver):

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Auth_link__1fOlj"))
        ).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Елена")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("elenanuryeva222@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(123456)

        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']"))
        )

        driver.find_element(*Locators.EMAIL).send_keys("elenanuryeva222@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

        print("Тест успешной регистрации пройден.")
        driver.quit()


    def test_registration_error_short_password(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Auth_link__1fOlj"))
        ).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys("Елена")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("elenanuryeva2188@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("1234")

        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((
                By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']"
            ))
        )

        assert error.is_displayed()
        print("Тест на некорректный пароль пройден.")

        driver.quit()

    def test_login_to_account_button(self, driver):
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

        print("Тест успешный вход в аккаунт через кнопку Войти в аккаунт пройден.")
        driver.quit()

    def test_login_to_account_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

        print("Тест успешный вход в аккаунт через личный кабинет пройден.")
        driver.quit()

    def test_login_to_account_personal_account_form_registration(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Auth_link__1fOlj"))
        ).click()

        driver.find_element(By.XPATH, "//a[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

        print("Тест успешный вход в аккаунт через форму регистрации пройден.")
        driver.quit()

def test_login_to_account_forgot_password(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        driver.find_element(By.XPATH, "//a[text()='Восстановить пароль']").click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Восстановить']"))
        )
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

        print("Тест успешный вход в аккаунт через кнопку в форме восстановления пароля пройден.")
        driver.quit()

def test_personal_account(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        driver.find_element(*Locators.EMAIL).send_keys("elenanuryeva2118@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")

        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        ).click()

        profile = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/account/profile']"))
        )

        assert "/account" in driver.current_url
        assert profile.text == "Профиль"

        print("Тест успешный переход личный кабинет пройден.")
        driver.quit()

def test_personal_account_go_to_constructor(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        driver.find_element(*Locators.EMAIL).send_keys("elenanuryeva2118@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")

        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/account/profile']"))
        )

        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.text_type_main-large.mb-5.mt-10"))
        )

        assert element.text == "Соберите бургер"

        print("Тест успешный переход из личного кабинета в конструктор пройден.")
        driver.quit()

def test_personal_account_go_to_logo(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        driver.find_element(*Locators.EMAIL).send_keys("elenanuryeva2118@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")
        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/account/profile']"))
        )

        driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.text_type_main-large.mb-5.mt-10"))
        )

        assert element.text == "Соберите бургер"

        print("Тест успешный переход из личного кабинета через лого в конструктор пройден.")
        driver.quit()

def test_personal_account_exit(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        driver.find_element(*Locators.EMAIL).send_keys("elenanuryeva2118@yandex.ru")
        driver.find_element(*Locators.PASSWORD).send_keys("123456")
        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/account/profile']"))
        )
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()

        profile_exit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )

        assert profile_exit.text == "Вход"

        print("Тест успешный выход из личного кабинета пройден.")
        driver.quit()

