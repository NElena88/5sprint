
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from curl import *
from helpers import generate_registration_account
from locators import Locators
from data import Texts


class TestSuccessfulRegistration:

    def test_successful_registration(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.LINK_REG))
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Texts.name_user)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_BUTTON)
        )

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

class TestRegistrationShortPassword:

    def test_registration_error_short_password(self, driver):
        email, password = generate_registration_account()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LINK_REG)
        ).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys(Texts.name_user)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("1234")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.REG_BUTTON))
        ).click()

        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ERR_PASSWORD)
        )

        assert error.is_displayed()

class TestLoginFromMainPage:

    def test_login_to_account_button(self, driver):
        driver.find_element(*Locators.LOGINACC_BUTT).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ENTRANCE)
        )

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

class TestLoginFromPersonalAccount:

    def test_login_to_account_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

class TestLoginFromRegistrationForm:

    def test_login_to_account_personal_account_form_registration(self, driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((Locators.LINK_REG))
        ).click()

        driver.find_element(*Locators.LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ENTRANCE)
        )

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

class TestLoginFromForgotPassword:

    def test_login_to_account_forgot_password(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        driver.find_element(*Locators.FORGOT_PASSW).click()

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.RECOVER_PASSW)
        )
        driver.find_element(*Locators.LOGIN_LINK).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        assert driver.current_url == main_site + 'login'

class TestPersonalAccountAccess:

    def test_personal_account(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.LINK_REG))
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Texts.name_user)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_BUTTON)
        )

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        profile = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PROFILE)
        )

        assert "/account" in driver.current_url
        assert profile.text == Texts.profile_heading

class TestGoToConstructor:

    def test_personal_account_go_to_constructor(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.LINK_REG))
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Texts.name_user)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_BUTTON)
        )

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PROFILE)
        )

        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.HEAD_CONSTRUC)
        )

        assert element.text == Texts.selection_food

class TestGoToMainFromLogo:

    def test_personal_account_go_to_logo(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.LINK_REG))
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Texts.name_user)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_BUTTON)
        )

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PROFILE)
        )

        driver.find_element(*Locators.LOGO_LINK).click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.HEAD_CONSTRUC)
        )

        assert element.text == Texts.selection_food

class TestLogout:

    def test_personal_account_exit(driver):
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.LINK_REG))
        ).click()

        email, password = generate_registration_account()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Texts.name_user)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENT_BUTTON)
        )

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC)
        ).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PROFILE)
        )
        driver.find_element(*Locators.EXIT_BUTTON).click()

        profile_exit = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ENTRANCE)
        )

        assert profile_exit.text == Texts.login_heading
