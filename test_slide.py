import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
base_url = 'http://automationpractice.com/index.php?id_category=3&controller=category#/'
browser.get(base_url)
browser.maximize_window()
action = ActionChains(browser)
slide_price = browser.find_element(By.XPATH, '//div[@id="layered_price_slider"]')
action.move_to_element(slide_price)
action.click_and_hold(slide_price).move_by_offset(15, 0).release().perform()
time.sleep(5)
browser.quit()
