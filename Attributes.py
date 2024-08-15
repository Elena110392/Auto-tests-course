from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(By.ID, 'treasure')
    x = element.get_attribute('valuex')
    value_print = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(value_print)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit.click()

finally:
    time.sleep(20)
    browser.quit()
