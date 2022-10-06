from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'


user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input Login')
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click Login Button')
menu = browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print('Click Menu Button')
link_about = browser.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print('Click Link About')
browser.quit()
