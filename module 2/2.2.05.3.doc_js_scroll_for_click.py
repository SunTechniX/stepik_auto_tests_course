from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

# Не знаю, писали ли ниже, но в этом случае можно справится без кода на Javascript. Для этого нужно использовать ActionChains:

driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")

try:
    button = driver.find_element(By.TAG_NAME, "button")
    #err: button = driver.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view

    button.click()
    assert True
    
finally:
    time.sleep(5)
    driver.quit() 
