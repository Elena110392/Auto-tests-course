from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.CSS_SELECTOR,"[id='input_value']").text
    answer = calc(x)
    input = browser.find_element(By.CSS_SELECTOR,'[id="answer"]')
    input.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR,'.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()