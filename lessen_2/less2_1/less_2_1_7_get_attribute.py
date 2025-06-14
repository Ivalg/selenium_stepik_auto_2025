import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://suninjuly.github.io/get_attribute.html'
driver = webdriver.Chrome()

try:
    driver.get(link)
    # Явное ожидание вместо time.sleep
    time.sleep(1)
    # Ищем элемент с атрибутом valuex (сундук)
    chest = driver.find_element('xpath', '//img[@id="treasure"]')
    x = chest.get_attribute('valuex')
    y = calc(x)
    # Заполняем форму
    driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)
    driver.find_element('xpath', '//input[@id="robotCheckbox"]').click()
    driver.find_element('xpath', '//input[@id="robotsRule"]').click()
    # Нажимаем Submit
    driver.find_element('xpath', '//button[@type="submit"]').click()


finally:
    time.sleep(5)
    # Правильное закрытие браузера
    driver.quit()