from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#查找单个元素
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
print(input_second)
print(input_third)

#browser.find_element(By.ID,"q")这里By.ID中的ID可以替换为其他几个
input_first = browser.find_element(By.ID, "q")
print(input_first)

#多个元素查找
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)

#元素交互操作
input_str = browser.find_element_by_id('q')
input_str.send_keys("ipad")
time.sleep(2)
input_str.clear()
input_str.send_keys("MakBook pro")
button = browser.find_element_by_class_name('btn-search')
browser.close()

