import time
from selenium import webdriver  # основной модуль Selenium
from selenium.webdriver.support.ui import Select  # для работы с выпадающими списками

link = 'https://suninjuly.github.io/selects1.html'  # URL страницы с тестом
driver = webdriver.Chrome()  # создаем экземпляр драйвера Chrome

try:
    driver.get(link)  # открываем страницу в браузере

    a = driver.find_element('xpath', '//span[@id="num1"]').text  # находим первое число
    b = driver.find_element('xpath', '//span[@id="num2"]').text  # находим второе число
    res = int(a) + int(b)  # вычисляем сумму чисел

    select = Select(driver.find_element('xpath', '//select[@id="dropdown"]'))  # находим выпадающий список
    select.select_by_value(str(res))  # выбираем вариант с нашей суммой
    driver.find_element('xpath', '//button[text()="Submit"]').click()  # нажимаем кнопку Submit
finally:
    time.sleep(5)  # пауза чтобы увидеть результат
    driver.quit()  # закрываем браузер