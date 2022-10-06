from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'


user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
# user_name.clear()  # используется для очищения поля
print('Input Login')
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print('Input password')
button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click Login Button')
text_products = browser.find_element(By.XPATH, '//span[@class="title"]')
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == 'PRODUCTS'
assert browser.current_url == 'https://www.saucedemo.com/inventory.html'
print('GOOD')
# Добавление скриншота и уникального имени для него через datetime
name_screenshot = 'screenshot-' + str(datetime.datetime.utcnow().strftime('%d.%m.%Y.%H.%M.%S')) + '.png'
# Создаем директорию Screen для добавления туда новых скриншотов
browser.save_screenshot('.\\Screen\\' + name_screenshot)
browser.quit()
