import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

@pytest.fixture(scope='session')
def browser():

    url = 'https://only.digital/'
    driver = webdriver.Chrome()
    driver.get(url)

    yield driver

    driver.quit()

def test_find_footer(browser):

    try:
        foot_check = browser.find_element(By.CLASS_NAME, 'Footer_root___6Q28')
        assert foot_check.is_enabled()
    except NoSuchElementException:
        assert False

def test_find_another_el_1(browser):

    try:
        el_check = browser.find_element(By.CLASS_NAME, 'copyrightsBig.FooterText_root___Rdpb')
        assert el_check.is_enabled()
    except NoSuchElementException:
        assert False

def test_find_another_el_2(browser):

    try:
        el_check = browser.find_element(By.CLASS_NAME, 'Socials_socialsWrap__DPtp_.Footer_socials__C39yX')
        assert el_check.is_enabled()
    except NoSuchElementException:
        assert False