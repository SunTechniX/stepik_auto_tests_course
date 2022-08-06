from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    browser.execute_script("alert('Lesson 2.3');")
    time.sleep(3)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()