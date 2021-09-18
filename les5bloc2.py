from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Name')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Last')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('sdf@sdfs.ru')
    current_dir = os.path.abspath(os.path.dirname('les5bloc2.py'))
    file_name = 'les5bloc2txt.txt'
    file_path = os.path.join(current_dir, file_name)
    send_file = browser.find_element_by_id('file')
    send_file.send_keys(file_path)
    button1 = browser.find_element_by_css_selector('button.btn')
    button1.click()
finally:
    time.sleep(5)
    browser.quit()