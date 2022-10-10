from selenium import webdriver
from selenium.webdriver.common.by import By

'''Драйвер у меня хранится на диске С и к нему указан путь через системную переменную XPath.
Поэтому я не передаю путь к драйверу.'''

print('Приветствуем Вас в нашем интернет магазине!')
print('Выберите один из следующих товаров и укажите его номер:\n1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light'
      '3 - Sauce Labs Bolt T-Shirt\n4 - Sauce Labs Fleece Jacket\n'
      '5 - Sauce Labs Onesie\n6 - Test.allTheThings() T-Shirt (Red)')
number_of_product = input('Ваш выбор: ')


# Открываем браузер
browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
browser.implicitly_wait(10)
print('Перешли на страницу интернет магазина')

try:
    # Проходим авторизацию
    user_name = browser.find_element(By.XPATH, '//input[@id="user-name"]')
    user_name.send_keys('standard_user')
    password = browser.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys('secret_sauce')
    button_login = browser.find_element(By.XPATH, '//input[@id="login-button"]')
    button_login.click()
    print('Авторизация пройдена')

    # Сохраняем информацию о выбранном пользователем товаре.
    # В XPATH путь передаем выбранный пользователем номер продукта
    '''Product Info'''
    name_of_product = browser.find_element(By.XPATH,
                                           f'//div[@class="inventory_list"]/div[{number_of_product}]/div[2]/div[1]/a')
    value_name_of_product = name_of_product.text
    price_of_product = \
        browser.find_element(By.XPATH, f'//div[@class="inventory_list"]/div[{number_of_product}]/div[2]/div[2]/div')
    value_price_of_product = price_of_product.text
    print('Сохранили название и цену выбранного товара')

    # Добавляем в корзину выбранный пользователем товар
    add_to_cart_button = \
        browser.find_element(By.XPATH, f'//div[@class="inventory_list"]/div[{number_of_product}]/div[2]/div[2]/button')
    add_to_cart_button.click()
    print('Добавили выбранный товар в корзину')

    # Проверяем, что в корзину добавлен 1 товар
    assert browser.find_element(By.XPATH, '//div[@id="shopping_cart_container"]').text == '1',\
        'В корзине неверное количество товаров!'

    # Переходим в корзину
    go_to_cart_button = browser.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
    go_to_cart_button.click()
    print('Перешли в корзину')

    # Проверяем, что в корзине находятся правильные товары
    assert browser.find_element(By.XPATH, '//div[@class="cart_item_label"]/a/div').text == value_name_of_product, \
        'Неверное название товара!'
    assert browser.find_element(By.XPATH,
                                '//div[@class="cart_item_label"]/div[2]/div').text \
           == value_price_of_product, 'Неверная цена товара!'
    print('Проверили название и цену товара в корзине')

    # Переходим на страницу подтверждения
    checkout_button = browser.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()
    print('Перешли на страницу подтверждения')

    # Заполняем информацию и переходим на следующую страницу
    first_name_field = browser.find_element(By.XPATH, '//input[@id="first-name"]')
    first_name_field.send_keys('Ivan')
    last_name_field = browser.find_element(By.XPATH, '//input[@id="last-name"]')
    last_name_field.send_keys('Ivanov')
    postal_code_field = browser.find_element(By.XPATH, '//input[@id="postal-code"]')
    postal_code_field.send_keys('1234')
    continue_button = browser.find_element(By.XPATH, '//input[@id="continue"]')
    continue_button.click()
    print('Заполнили личные данные и перешли на следующую страницу')

    # Проверяем, что на странице подтверждения заказа находятся правильный товар
    assert browser.find_element(By.XPATH, '//div[@class="cart_item_label"]/a/div').text == value_name_of_product, \
        'Неверное название товара!'
    assert browser.find_element(By.XPATH,
                                '//div[@class="cart_item_label"]/div[2]/div').text \
           == value_price_of_product, 'Неверная цена товара!'
    print('Проверили названия и цены товаров на странице подтверждения заказа')

    # Проверяем сумму товара
    item_total = browser.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
    value_item_total = item_total.text
    value_price_of_product = float(value_price_of_product[1:])
    value_price_of_product = f'Item total: ${value_price_of_product}'
    assert value_item_total == value_price_of_product, 'Неверная сумма заказа!'
    print('Проверили сумму заказа')

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
