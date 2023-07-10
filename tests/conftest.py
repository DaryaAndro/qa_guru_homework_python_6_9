import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    driver_options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = driver_options

    yield

    browser.quit()
