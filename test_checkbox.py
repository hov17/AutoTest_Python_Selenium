from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
base_url = 'https://demoqa.com/checkbox/'
browser.get(base_url)
browser.maximize_window()
# Нажимаешь на чекбокс
checkbox = browser.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
checkbox.click()
# Раскрываем список чекбокса
checkbox_menu = browser.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
checkbox_menu.click()
browser.quit()
