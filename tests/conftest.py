import pytest
import requests


from curl import *
from locators import Locators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from data import Credentials


@pytest.fixture(scope="function")
def driver():
    # Создаем опции для Chrome
    options = Options()
    options.add_argument("--window-size=1200,600")  # Задаем размер окна

    # Инициализируем драйвер (путь к нему должен быть в PATH)
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(main_site)

    yield driver
    driver.quit()
