from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

name_form = '//*[@id="input-1"]'
email_form = '//*[@id="input-2"]'
username_form = '//*[@id="input-3"]'
password_form = '//*[@id="input-4"]'
confirm_form = '//*[@id="input-5"]'
signup_with_email = '//*[@id="form-register"]/div/a[2]'
    
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stockbit.com/#/register')
    yield driver
    driver.quit()

def test_RegisterWithNullData(driver):
    register_btn = '//*[@id="form-register"]/div/input'
    hint = '//*[@id="form-register"]/div/div[1]/div[2]/span'
    expected_hint = 'Using your real name makes it easier for you to be recognised and build a network.'
    
    driver.find_element_by_xpath(signup_with_email).click()
    driver.find_element_by_xpath(register_btn).click()
    assert expected_hint in driver.find_element_by_xpath(hint).text

def test_InvalidEmailFormat(driver):
    err_msg = '//*[@id="form-register"]/div/div[2]/span'
    expected_msg = 'Format email salah'

    driver.find_element_by_xpath(signup_with_email).click()
    driver.find_element_by_xpath(email_form).send_keys('asd')
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.XPATH, err_msg)))
    assert expected_msg in driver.find_element_by_xpath(err_msg).text

def test_InvalidPassFormat(driver):
    err_msg = '//*[@id="form-register"]/div/div[4]/div[1]/span'
    expected_msg = 'value harus terdiri dari minimal 6 karakter'

    driver.find_element_by_xpath(signup_with_email).click()
    driver.find_element_by_xpath(password_form).send_keys('asd')
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.XPATH, err_msg)))
    assert expected_msg in driver.find_element_by_xpath(err_msg).text

def test_PassDoesntMatch(driver):
    err_msg = '//*[@id="form-register"]/div/div[4]/div[2]/span'
    expected_msg = 'Password does not match'

    driver.find_element_by_xpath(signup_with_email).click()
    driver.find_element_by_xpath(name_form).send_keys('dimas')
    driver.find_element_by_xpath(email_form).send_keys('dimas_m90@yahoo.com')
    driver.find_element_by_xpath(username_form).send_keys('dimasmahendrap')
    driver.find_element_by_xpath(password_form).send_keys('Qwerty123@')
    driver.find_element_by_xpath(confirm_form).send_keys('asd')
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.XPATH, err_msg)))
    assert expected_msg in driver.find_element_by_xpath(err_msg).text