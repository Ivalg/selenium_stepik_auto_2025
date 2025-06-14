from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

try:
    driver.get('http://suninjuly.github.io/wait2.html')
    button = wait.until(EC.element_to_be_clickable(('xpath', '//button[@id="verify"]')))
    button.click()
    message = driver.find_element('xpath', '//div[@id="verify_message"]')

    assert message.text == 'Verification was successful!'

finally:
    driver.quit()