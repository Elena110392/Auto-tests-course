from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    int_x = int(x)
    calc_x = calc(int_x)
    print(calc_x)
    input_field = browser.find_element(By.ID, 'answer')
    browser.execute_script('arguments[0].scrollIntoView(true);', input_field)
    input_field.send_keys(calc_x)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR,"[for='robotsRule']")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
finally:
    time.sleep(10)
    browser.quit()