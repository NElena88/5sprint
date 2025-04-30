
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from helpers import generate_registration_account
from locators import Locators
from curl import *
from selenium.webdriver.common.by import By



class TestConstructor:

    def test_constructor_tabs_sauces(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()

        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")
        assert active_tab.text == "Соусы"
        driver.quit()

    def test_constructor_tabs_toppings(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))).click()
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")
        assert active_tab.text == "Начинки"
        driver.quit()

    def test_constructor_tabs_rolls(self, driver):
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']"))
        )
        driver.find_element(By.XPATH, "//span[text()='Булки']")

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Булки']"))
        )
        assert active_tab.text == "Булки"
        driver.quit()
