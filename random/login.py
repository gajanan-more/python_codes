from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# connect to google.com
driver = webdriver.Chrome(options=Options())

def login(username, password):

    driver.get("https://dndnewcallistoui.login.stage.akamai-access.com")

#     # find the search input field
#     # id="username"
#     username_f = driver.find_element("id", "username")
#
#     # type the search string
#     username_f.send_keys(username)
#
#     password_f = driver.find_element("id", "password")
#
#     password_f.send_keys(password)
#
#     login_button = driver.find_element("id", "cal-login-button")
#
#     login_button.click()
#
#
# login("1_testuser@gmail.com", "Akamai@1231")
