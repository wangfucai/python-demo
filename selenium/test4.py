from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")

#获取元素属性
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

#获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

#获取ID，位置，标签名
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

#执行JavaScript
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')