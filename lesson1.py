import time 

#webdriver это набор команд для управления браузером
from selenium import webdriver

#инициализируем драйвер браузера. После этой команды должно появиться новое окно браузера
driver = webdriver.Chrome()

#Команда time.sleep() устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

#метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get('https://stepik.org/lesson/25969/step/12')
time.sleep(5)

#метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему.
#ищет поле для ввода текста
textarea = driver.find_element_by_css_selector('.textarea')

#напишем текст для ответа в найденое поле
textarea.send_keys('get()')
time.sleep(5)

#найдем кнопку которая отправляет введенное сообщение
submit_button = driver.find_element_by_css_selector('.submit-submission')

#скажем драйверу, что нужно нажать на кнопку
submit_button.click()
time.sleep(5) 

#после выполнения всех действий необходимо закрыть окно
driver.quit()
