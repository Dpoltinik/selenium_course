from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('.trollface')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    input_value = browser.find_element_by_id('input_value')
    value = input_value.text
    answer = calc(int(value))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(answer)

    button2 = browser.find_element_by_css_selector('button.btn')
    button2.click()

finally:

    time.sleep(10)
    browser.quit()