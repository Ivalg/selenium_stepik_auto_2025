import math  # импорт модуля math
import time  # импорт модуля time
from selenium import webdriver  # импорт webdriver из selenium

driver = webdriver.Chrome()  # инициализация драйвера Chrome


def calc(x):  # функция вычисления формулы: log|12*sin(x)|
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get('https://suninjuly.github.io/redirect_accept.html')  # открытие страницы
#    window_1 = driver.window_handles[0]  # сохранение идентификатора первой вкладки
    driver.find_element('xpath', '//button[@class="trollface btn btn-primary"]').click()  # клик по кнопке
    window_2 = driver.window_handles[-1]  # сохранение идентификатора новой вкладки
    driver.switch_to.window(window_2)  # переключение на новую вкладку

    x = driver.find_element('xpath', '//span[@id="input_value"]').text  # получение значения x
    y = calc(x)  # вычисление y по формуле
    driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)  # ввод ответа в поле
    driver.find_element('xpath', '//button[@class="btn btn-primary"]').click()  # отправка формы
finally:
    time.sleep(5)  # задержка перед закрытием браузера
    driver.quit()  # закрытие браузера