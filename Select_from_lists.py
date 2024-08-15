from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, 'num1').text
    num_2 = browser.find_element(By.ID, 'num2').text
    int_num1 = int(num_1)
    int_num2 = int(num_2)
    sum = (int_num1 + int_num2)
    textsum = str(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(textsum)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
