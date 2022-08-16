import time
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []
with webdriver.Chrome() as browser:
        for x in range(1, 7):
            blank = browser.execute_script(f'window.open("http://parsinger.ru/blank/1/{x}.html", "_blank{x}");')
        tabs = browser.window_handles
        for z in range(len(tabs) - 1):
            if not browser.execute_script("return document.title;"):
                browser.close()
            time.sleep(1)
            browser.switch_to.window(browser.window_handles[z])
            browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
            result.append(int(browser.find_element(By.ID, 'result').text))
            print(browser.find_element(By.ID, 'result').text)
print(result)