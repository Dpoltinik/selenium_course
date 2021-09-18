from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    sum = int(num1.text) + int(num2.text)

    input1 = browser.find_element_by_id('dropdown')
    input1.send_keys(sum)
    button1 = browser.find_element_by_css_selector('button.btn')
    button1.click()
finally:
    time.sleep(5)
    browser.quit()
    