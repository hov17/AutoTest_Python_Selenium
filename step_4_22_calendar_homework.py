import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''С помощью модуля datetime прибавляем к текущей дате 10 дней'''
future_date = datetime.date.today() + datetime.timedelta(days=10)

print('Открываем браузер')
browser = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
browser.get(base_url)
browser.maximize_window()
print('Перешли на сайт')
try:
    select_date_field = browser.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
    select_date_field.send_keys(Keys.BACKSPACE * 10)
    print('Удалили текущую дату')
    select_date_field.send_keys(str(future_date))
    select_date_field.send_keys(Keys.RETURN)
    print('Ввели будущую дату')
    time.sleep(5)
finally:
    browser.quit()
