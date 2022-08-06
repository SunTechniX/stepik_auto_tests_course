from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img_el = browser.find_element(By.ID, 'treasure')
    x = img_el.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    chkbox = browser.find_element(By.ID, 'robotCheckbox')
    chkbox.click()
    
    radiobox = browser.find_element(By.ID, 'robotsRule')
    radiobox.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
