from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
base_url = 'https://demoqa.com/dynamic-properties'
browser.get(base_url)
browser.maximize_window()
# browser.implicitly_wait(10)  # Неявное ожидание
invisible_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable  # Явное ожидание
                                                    ((By.XPATH, '//button[@id="visibleAfter"]')))
invisible_button.click()
browser.quit()
