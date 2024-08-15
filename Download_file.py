from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = 'https://suninjuly.github.io/file_input.html'
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Helen')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Ivanova')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('Ivanova@mail.com')
    file_input = browser.find_element(By.CSS_SELECTOR, '[id="file"]')
    file_path = 'D:\\File.txt'
    file_input.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
