from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# I'm using Microsoft Edge. So it won't work if you use another browser


browser = webdriver.Edge("") # insert your webdriver path into the string

browser.get("https://www.instagram.com")

time.sleep(5)

# log in operations

userName = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
logIn = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

# Sending the keys

userName.send_keys("") #insert your username into the string
time.sleep(1)
password.send_keys("") #insert your password into the string
time.sleep(1)

# Clicking the login button after sended the parameters

logIn.click()


