from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

'''Скроллинг экрана. X и Y количество пикселей по горизонтали и вертикали соответственно'''
# browser.execute_script('window.scrollTo(X, Y)')

'''Переход к определенному элементу'''
# action = ActionChains(browser)
# red_t_shirt = browser.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
# action.move_to_element(red_t_shirt).perform()
browser.quit()
