from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

urls  = {'old': 'http://suninjuly.github.io/registration1.html', 'new': 'http://suninjuly.github.io/registration2.html'}

for k,v in urls.items():
    try: 
        link = v
        browser = webdriver.Chrome()
        browser.get(link)
        
        # '//input[@placeholder="Input your first name"]'
        # fisrt_name  /html/body/div/form/div[1]/div[1]/input
        browser.find_element(By.XPATH, '//form/div[1]/div[1]/input').send_keys('John')
        time.sleep(1)
        # last_name
        browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('Wick')
        time.sleep(.7)

        # e-mail
        browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('johnwick@dev.by')

        time.sleep(5)

        # Отправляем заполненную форму
        action = ActionChains(browser)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        action.move_to_element(button).perform()

        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(welcome_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    except Exception as e:
        print(f"Test for \"{k}\" page has failed!\n\
         Exception infor: {e} has been catched!")
    else:
        print(f"Test for \"{k}\" page has been passed!")
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        print("Tests finished!")
        # закрываем браузер после всех манипуляций
        browser.quit()