
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Texts
from helpers import generate_registration_account
from locators import Locators
from curl import *
from selenium.webdriver.common.by import By


class TestConstructorSauces:

    def test_constructor_tabs_sauces(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SECTION_SAUCES)).click()

        active_tab = driver.find_element(*Locators.HEADER_SAUC)
        assert active_tab.text == Texts.sous_tab

class TestConstructorToppings:

    def test_constructor_tabs_toppings(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SECTION_TOPPIN)).click()
        active_tab = driver.find_element(*Locators.HEADER_TOPPIN)
        assert active_tab.text == Texts.toppings_tab

class TestConstructorRolls:

    def test_constructor_tabs_rolls(self, driver):
        driver.find_element(*Locators.SECTION_SAUCES).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.HEADER_SAUC)
        )
        driver.find_element(*Locators.SECTION_ROLLS)

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.HEADER_ROLLS)
        )
        assert active_tab.text == Texts.rolls_tab
