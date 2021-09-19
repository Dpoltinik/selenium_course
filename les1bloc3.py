from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By


class SuccesRef(unittest.TestCase):
    def test1(self):
        
        link_succes = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        # browser.get(link_failure)
        browser.get(link_succes)

        name_input = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .first')
        name_input.send_keys('Dima')
        lastname_input = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .second')
        lastname_input.send_keys('Poltavcev')
        email_input = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .third')
        email_input.send_keys('sdf@sdjf.ro')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        succes_text = browser.find_element(By.TAG_NAME, 'h1')
        text = succes_text.text
        
        self.assertEqual('Congratulations! You have successfully registered!', text, 'Все поломано кеп')
    
    def test2(self):
        
        link_failure = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        # browser.get(link_failure)
        browser.get(link_failure)

        name_input = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .first')
        name_input.send_keys('Dima')
        lastname_input = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .second')
        lastname_input.send_keys('Poltavcev')
        email_input = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .third')
        email_input.send_keys('sdf@sdjf.ro')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        succes_text = browser.find_element(By.TAG_NAME, 'h1')
        text = succes_text.text
        self.assertEqual('Congratulations! You have successfully registered!', text, 'fffffffffffffffffffffffffff')

if __name__ == '__main__':
    unittest.main()



