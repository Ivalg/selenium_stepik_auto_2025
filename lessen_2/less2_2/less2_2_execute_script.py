import math  # модуль для математических операций
import time  # модуль для временных задержек

from selenium import webdriver  # модуль для автоматизации браузера


def calc(x):  # функция вычисления формулы
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()  # инициализация драйвера Chrome
link = "https://SunInJuly.github.io/execute_script.html"  # URL тестовой страницы

try:
    driver.get(link)  # открываем страницу в браузере
    x = driver.find_element('xpath', '//span[@id="input_value"]').text  # получаем значение X
    y = calc(x)  # вычисляем результат по формуле
    driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)  # вводим ответ в поле

    check_box = driver.find_element('xpath', '//input[@id="robotCheckbox"]')  # находим чекбокс
    driver.execute_script('return arguments[0].scrollIntoView(true);', check_box)  # скроллим к чекбоксу
    check_box.click()  # кликаем чекбокс

    radio = driver.find_element('xpath', '//input[@id="robotsRule"]')  # находим радиобатон
    driver.execute_script('return arguments[0].scrollIntoView(true);', radio)  # скроллим к радиобатону
    radio.click()  # выбираем радиобатон

    button = driver.find_element('xpath', '//button[@class="btn btn-primary"]')  # находим кнопку
    driver.execute_script('return arguments[0].scrollIntoView(true);', button)  # скроллим к кнопке
    button.click()  # нажимаем кнопку

finally:
    time.sleep(5)  # пауза перед закрытием браузера
    driver.quit()  # корректное закрытие браузера