from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    answer.send_keys(y)

    chkbox = browser.find_element(By.CSS_SELECTOR, 'input[id = "robotCheckbox"]')
    chkbox.click()
    
    radiobox = browser.find_element(By.CSS_SELECTOR, 'input[id = "robotsRule"]')
    radiobox.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
