import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
browser.get(base_url)
browser.maximize_window()
# Очищение поля и введение новой даты
select_date_field = browser.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
select_date_field.send_keys(Keys.BACKSPACE * 10)
select_date_field.send_keys('10/06/2022')
select_date_field.send_keys(Keys.RETURN)
browser.quit()
