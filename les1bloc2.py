from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id('input_value')
    input_text = input1.text 

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x = calc(int(input_text))

    input2 = browser.find_element_by_id('answer')
    input2.send_keys(x)
    input3 = browser.find_element_by_id('robotCheckbox')
    input3.click()
    input4 = browser.find_element_by_id('robotsRule')
    input4.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

