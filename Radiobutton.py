from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value')
    value = x.text
    value_print = calc(value)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(value_print)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR,".btn-default")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

