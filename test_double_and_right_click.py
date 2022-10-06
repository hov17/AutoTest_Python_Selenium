import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
base_url = 'https://demoqa.com/buttons'
browser.get(base_url)
browser.maximize_window()
action = ActionChains(browser)
# Двойное нажатие ЛКМ
double_click_button = browser.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double_click_button).perform()
# Нажатие ПКМ
right_click_button = browser.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_click_button).perform()
time.sleep(5)
browser.quit()
