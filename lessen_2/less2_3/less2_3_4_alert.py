import math
import time
from selenium import webdriver

driver = webdriver.Chrome()


def calc(x):  # функция вычисления формулы
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get('https://suninjuly.github.io/alert_accept.html')
    driver.find_element('xpath', '//button[@class="btn btn-primary"]').click()
    alert = driver.switch_to.alert
    alert.accept()

    x = driver.find_element('xpath', '//span[@id="input_value"]').text
    y = calc(x)
    driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)
    driver.find_element('xpath', '//button[@class="btn btn-primary"]').click()

finally:
    time.sleep(3)
    driver.quit()

