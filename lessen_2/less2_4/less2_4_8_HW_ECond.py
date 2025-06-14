import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 12)


def calc(x):  # функция вычисления формулы
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    price = wait.until(EC.text_to_be_present_in_element(('xpath', '//h5[@id="price"]'), '$100'))
    wait.until(EC.element_to_be_clickable(('xpath', '//button[@id="book"]'))).click()

    x = driver.find_element('xpath', '//span[@id="input_value"]').text
    y = calc(x)
    driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)
    driver.find_element('xpath', '//button[@id="solve"]').click()


finally:
    time.sleep(5)
    driver.quit()
