import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

    
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_basket_button(browser):
    browser.get(link)
    time.sleep(5) # добавить 30с для визуальной проверки работоспособности разных языков 
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert button, 'No such button'
   

