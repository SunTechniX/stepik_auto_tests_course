import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action="store", default=None,
                     help="Choose language: ru, fr ...")

@pytest.fixture(scope="function") #фикстура browser
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    
    if browser_name =="chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  #выбор языка Chrome
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome for test..")
               
    elif browser_name == "firefox":
        browser = webdriver.Firefox(firefox_profile=fp)
        #выбор языка пользователя для Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    
    yield browser
    print("\nquit browser..")
    browser.quit()
