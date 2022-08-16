from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    browser.execute_script("confirm('Lesson 2.3');")
    time.sleep(3)
    confirm = browser.switch_to.alert
    confirm_text = confirm.text
    print(confirm_text)
    # confirm.accept()
    confirm.dismiss()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()