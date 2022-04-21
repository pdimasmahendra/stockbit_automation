from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stockbit.com/')
    yield driver
    driver.quit()

def test_InvestingMenu(driver):
    investing_menu = '//*[@id="landing-wrapper"]/div[1]/div/div[2]/div/div[2]/a[1]'
    expected_text1 = 'Daftar 100% Online'
    

    driver.find_element_by_xpath(investing_menu).click()
    assert expected_text1 in driver.find_element_by_css_selector('h1').text

def test_ProToolsMenu(driver):
    protools_menu = '//*[@id="landing-wrapper"]/div[1]/div/div[2]/div/div[2]/a[2]'
    expected_text2 = 'Professional Tools'

    driver.find_element_by_xpath(protools_menu).click()
    assert expected_text2 in driver.find_element_by_css_selector('h1').text

def test_AboutUsMenu(driver):
    aboutus_menu = '//*[@id="landing-wrapper"]/div[1]/div/div[2]/div/div[2]/a[4]'
    expected_text3 = 'Informasi Perusahaan'

    driver.find_element_by_xpath(aboutus_menu).click()
    assert expected_text3 in driver.find_element_by_css_selector('h3').text


    




    
        
        

    

