from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def createDriverInstance():
    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    except Exception as e:
        print(e)