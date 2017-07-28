from selenium import webdriver

#访问页面
browser = webdriver.Chrome()
browser.get("http://www.baidu.com");
print(browser.page_source)
browser.close()
