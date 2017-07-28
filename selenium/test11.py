from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#异常处理
#http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()