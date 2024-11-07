import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import pickle
driver = webdriver.Chrome()

def login(driver):
    #SAVE COOKIE
    pickle.dump(driver.get_cookies(), open("cookies.pickle", "wb"))
    time.sleep(2)

    email_input = driver.find_element(By.ID, "LoginForm_email")
    password_input = driver.find_element(By.ID, "LoginForm_password")
    email_input.send_keys(input("Your Email:"))
    password_input.send_keys(input("Your Password:"))
    login_button = driver.find_element(By.CLASS_NAME, "login__button")
    login_button.click()
    time.sleep(5)

#ACCESS WEBSITE
driver.get("https://www.zalora.co.id/customer/account/login/?from=header")

#Checking Cookies 
try:
    #LOAD
    cookies = pickle.load(open("cookies.pickle", "rb"))
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
except Exception as e:
    login(driver)
    pass

buttoncha = driver.find_element(By.ID, "px-captcha")
ActionChains(driver)\
        .click_and_hold(buttoncha)\
        .perform()
time.sleep(1000)
