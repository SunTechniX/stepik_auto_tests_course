# pytest -v -s --language=es test_items.py
# pytest -v -s --language=fr test_items.py

from selenium.webdriver.common.by import By
import time

def test_button_present(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed(), "The button Add to cart is missing"

#    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').is_enabled(), "The button Add to cart is missing"
