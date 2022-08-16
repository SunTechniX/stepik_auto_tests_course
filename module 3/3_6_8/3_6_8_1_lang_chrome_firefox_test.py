# pytest -s -v --browser_name=firefox 3_6_8_lang_chrome_firefox_test.py
# pytest -s -v --language=en --browser_name=firefox 3_6_8_lang_chrome_firefox_test.py

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser, langauge):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")