from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x = browser.find_element_by_id('input_value')
    answer = calc(int(x.text))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(answer)
    RoboChek = browser.find_element_by_id('robotCheckbox')
    RoboChek.click()
    RoboRadio = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', RoboRadio)
    RoboRadio.click()
    button1 = browser.find_element_by_css_selector('button.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true)', button1)
    button1.click()
finally:
    time.sleep(5)
    browser.quit()