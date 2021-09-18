from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element_by_id('treasure')
    treasure_num = treasure_img.get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    answer = calc(int(treasure_num))
    
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)
    field_Checkbox = browser.find_element_by_id('robotCheckbox')
    field_Checkbox.click()
    field_Radiobox = browser.find_element_by_id('robotsRule')
    field_Radiobox.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
        