from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

email_form = '//*[@id="username"]'
password_form = '//*[@id="password"]'
login_btn = '//*[@id="loginbutton"]'
alert = '//*[@id="main-wrapper"]/div[3]/div'
    
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stockbit.com/#/login')
    yield driver
    driver.quit()

def test_LoginWithInvalidData(driver):
    expected_alert = 'Username atau password salah'

    driver.find_element_by_xpath(email_form).send_keys('asd')
    driver.find_element_by_xpath(password_form).send_keys('asd')
    driver.find_element_by_xpath(login_btn).click()

    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.XPATH, alert)))
    assert expected_alert in driver.find_element_by_xpath(alert).text