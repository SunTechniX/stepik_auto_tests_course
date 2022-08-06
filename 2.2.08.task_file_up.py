from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try: 
    browser.get(link)

    fname = browser.find_element(By.NAME, "firstname")
    fname.send_keys("Ivan")

    lname = browser.find_element(By.NAME, "lastname")
    lname.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("x@x.x")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    xfile_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    xfile = browser.find_element(By.ID, "file")
    xfile.send_keys(xfile_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
