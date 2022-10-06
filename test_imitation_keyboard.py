from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'


user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input Login')
# user_name.send_keys(Keys.BACKSPACE)  # удаление символа
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
password.send_keys(Keys.RETURN)  # клавиша Enter
drop_down = browser.find_element(By.XPATH, '//select[@class="product_sort_container"]')
drop_down.click()
print('Click DropDown')
drop_down.send_keys(Keys.DOWN)  # спуск на одну позицию в выпадающем списке
drop_down.send_keys(Keys.RETURN)
# button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
# button_login.click()
# print('Click Login Button')
browser.quit()
