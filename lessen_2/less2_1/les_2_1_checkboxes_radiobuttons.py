import time

from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

link = 'https://suninjuly.github.io/math.html'

try:
    driver.get(link)
    x = driver.find_element('xpath', '//span[@id="input_value"]').text
    y = calc(x)
    driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)
    driver.find_element('xpath', '//input[@id="robotCheckbox"]').click()
    driver.find_element('xpath', '//input[@id="robotsRule"]').click()
    driver.find_element('xpath', '//button[@class="btn btn-default"]').click()

finally:
    time.sleep(5)
    driver.quit()



