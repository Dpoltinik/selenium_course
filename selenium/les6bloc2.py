from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('button.btn')
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x = browser.find_element_by_id('input_value')
    answer = calc(int(x.text))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(answer)
    button2 = browser.find_element_by_css_selector('button.btn')
    button2.click()



finally:

    time.sleep(15)
    browser.quit()


