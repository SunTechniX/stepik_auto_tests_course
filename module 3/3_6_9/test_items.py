# pytest --language=es test_items.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_present_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket'))
    )
    assert button is not None, "There is Basket button?"
