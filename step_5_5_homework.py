from selenium import webdriver
from selenium.webdriver.common.by import By

users_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
browser.implicitly_wait(10)
print('Перешли на страницу интернет магазина')

try:
    for user in users_list:
        # Проходим авторизацию за всех пользователей
        if user not in 'locked_out_user':
            user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
            user_name.send_keys(user)
            password = browser.find_element(By.XPATH, '//input[@id="password"]')
            password.send_keys('secret_sauce')
            button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
            button_login.click()
            assert browser.current_url == 'https://www.saucedemo.com/inventory.html', \
                'Авторизация не пройдена! Неверный адрес страницы'
            burger_menu_button = browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
            burger_menu_button.click()
            logout_link = browser.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
            logout_link.click()
            assert browser.current_url == 'https://www.saucedemo.com/', 'Разлогин не выполнен! Неверный адрес страницы!'
            print(f'Тест за пользователя {user} успешно пройден')
        else:
            user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
            user_name.send_keys(user)
            password = browser.find_element(By.XPATH, '//input[@id="password"]')
            password.send_keys('secret_sauce')
            button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
            button_login.click()
            error_button = browser.find_element(By.XPATH, '//button[@class="error-button"]')
            error_button.click()
            browser.refresh()
            print(f'Тест за пользователя {user} успешно пройден')
finally:
    browser.quit()
print('Тест успешно завершен!')
