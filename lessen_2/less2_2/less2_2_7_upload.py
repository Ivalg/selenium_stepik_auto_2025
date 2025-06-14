import os
import time

from selenium import webdriver

driver = webdriver.Chrome()

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file_up.txt')
data = ['Ivan', 'Ivanov', 'test123@mail.com']
try:

    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element('xpath', '//input[@placeholder="Enter first name"]').send_keys(data[0])
    driver.find_element('xpath', '//input[@placeholder="Enter last name"]').send_keys(data[1])
    driver.find_element('xpath', '//input[@placeholder="Enter email"]').send_keys(data[2])
    driver.find_element('xpath', '//input[@id="file"]').send_keys(file_path)
    driver.find_element('xpath', '//button[text()="Submit"]').click()

finally:
    time.sleep(5)
    driver.quit()
