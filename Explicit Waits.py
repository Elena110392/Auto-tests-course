from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    x = browser.find_element(By.CSS_SELECTOR,"[id='input_value']").text
    answer = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, '[id="solve"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()