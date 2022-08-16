from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    browser.execute_script("prompt('Lesson 2.3');")
    time.sleep(1)
    prompt = browser.switch_to.alert
    prompt_text = prompt.text
    print(prompt_text)
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    time.sleep(3)
    prompt.accept()    
    # prompt.dismiss()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()