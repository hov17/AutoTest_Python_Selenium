from selenium import webdriver
from selenium.webdriver.common.by import By

'''Драйвер у меня хранится на диске С и к нему указан путь через системную переменную XPath.
Поэтому я не передаю путь к драйверу.'''

# Открываем браузер
browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()

try:
    login_standard_user = 'standard_user'
    password_all = 'secret_sauce'

    # Проходим авторизацию
    user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
    user_name.send_keys(login_standard_user)
    print('Ввели логин')
    password = browser.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys(password_all)
    print('Ввели пароль')
    button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
    button_login.click()
    print('Нажали кнопку Войти')

    # Сохраняем информацию о товарах
    '''Product Info'''
    name_of_product1 = browser.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
    value_name_of_product1 = name_of_product1.text
    price_of_product1 = browser.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
    value_price_of_product1 = price_of_product1.text
    name_of_product2 = browser.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
    value_name_of_product2 = name_of_product2.text
    price_of_product2 = browser.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
    value_price_of_product2 = price_of_product2.text
    print('Информация о товарах получена')

    # Добавляем товары в корзину
    add_to_cart_product1 = browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    add_to_cart_product1.click()
    add_to_cart_product2 = browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    add_to_cart_product2.click()
    print('Товары добавлены в корзину')

    # Проверяем, что в корзину добавлено два товара
    assert browser.find_element(By.XPATH, '//div[@id="shopping_cart_container"]').text == '2', \
        'В корзине неверное количество товаров!'

    # Переходим в корзину
    go_to_cart_button = browser.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
    go_to_cart_button.click()
    print('Перешли в корзину')

    # Проверяем, что в корзине находятся правильные товары
    assert browser.find_element(By.XPATH, '//a[@id="item_1_title_link"]').text == value_name_of_product1, \
        'Неверное название первого товара!'
    assert browser.find_element(By.XPATH,
                                '//div[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text \
           == value_price_of_product1, 'Неверная цена первого товара!'
    assert browser.find_element(By.XPATH, '//a[@id="item_5_title_link"]').text == value_name_of_product2, \
        'Неверное название второго товара!'
    assert browser.find_element(By.XPATH,
                                '//div[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text \
           == value_price_of_product2, 'Неверная цена второго товара!'
    print('Проверили названия и цены товаров в корзине')

    # Переходим на страницу подтверждения
    checkout_button = browser.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()
    print('Перешли на страницу подтверждения')

    # Заполняем информацию и переходим на следующую страницу
    first_name_field = browser.find_element(By.XPATH, '//input[@id="first-name"]')
    first_name_field.send_keys('Ivan')
    print('Ввели имя')
    last_name_field = browser.find_element(By.XPATH, '//input[@id="last-name"]')
    last_name_field.send_keys('Ivanov')
    print('Ввели фамилию')
    postal_code_field = browser.find_element(By.XPATH, '//input[@id="postal-code"]')
    postal_code_field.send_keys('1234')
    print('Ввели код')
    continue_button = browser.find_element(By.XPATH, '//input[@id="continue"]')
    continue_button.click()
    print('Перешли на следующую страницу')

    # Проверяем, что на странице подтверждения заказа находятся правильные товары
    assert browser.find_element(By.XPATH, '//a[@id="item_1_title_link"]').text == value_name_of_product1, \
        'Неверное название первого товара!'
    assert browser.find_element(By.XPATH,
                                '//div[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text \
           == value_price_of_product1, 'Неверная цена первого товара!'
    assert browser.find_element(By.XPATH, '//a[@id="item_5_title_link"]').text == value_name_of_product2, \
        'Неверное название второго товара!'
    assert browser.find_element(By.XPATH,
                                '//div[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text \
           == value_price_of_product2, 'Неверная цена второго товара!'
    print('Проверили названия и цены товаров на странице подтверждения заказа')

    # Проверяем общую сумму товаров
    item_total = browser.find_element(By.XPATH, '//div[@id="checkout_summary_container"]/div/div[2]/div[5]')
    value_item_total = item_total.text
    value_price_of_product1 = float(value_price_of_product1[1:])
    value_price_of_product2 = float(value_price_of_product2[1:])
    total_value_price = f'Item total: ${value_price_of_product1 + value_price_of_product2}'
    assert value_item_total == total_value_price, 'Неверная общая сумма товаров!'
    print('Проверили общую сумму заказа на странице подтверждения заказа')

    # Переходим на страницу завершения заказа
    finish_button = browser.find_element(By.XPATH, '//button[@id="finish"]')
    finish_button.click()
    print('Перешли на страницу завершения заказа')

    # Проверяем что мы на странице завершения заказа и возвращаемся на главную страницу
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html',\
        'Неверный адрес страницы завершения заказа!'
    print('Все шаги успешно пройдены')
finally:
    browser.quit()
