from selenium.webdriver.common.by import By
import pytest
import time


def test_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert browser.find_element(By.XPATH, "//button[@value='Добавить в корзину']"), 'There is no add to cart button'