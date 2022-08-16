import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def answer():
    return math.log(int(time.time()))

lilink = ['https://stepik.org/lesson/236895/step/1',
          'https://stepik.org/lesson/236896/step/1',
          'https://stepik.org/lesson/236897/step/1',
          'https://stepik.org/lesson/236898/step/1',
          'https://stepik.org/lesson/236899/step/1',
          'https://stepik.org/lesson/236903/step/1',
          'https://stepik.org/lesson/236904/step/1',
          'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('links', lilink)
def test_aliens_msg(browser, links):
    link = links
    browser.get(link)

    # time.sleep(2)

    #area = browser.find_element(By.ID, 'ember99')
    area = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[required]'))
    )  # ex: element_to_be_selected
    print('Find ember+99')
    area.send_keys(answer())

    #time.sleep(1)

    # говорим Selenium проверять в течение 5 мл.секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="submit-submission"]'))
    )
    print('Find Clickable Button')
    button.click()

    #time.sleep(1)

    # говорим Selenium проверять в течение 5 мл.секунд
    amessage = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="smart-hints__hint"]'))
    )  # ex: text_to_be_present_in_element
    print('Find A-Message')
    print(amessage.text)
    assert amessage.text == 'Correct!', "NOT Correct Answer!"
