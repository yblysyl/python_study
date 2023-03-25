'''
安装库：
pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/  selenium  ##这样子快,出错少


下载浏览器驱动
Chrome:	http://chromedriver.storage.googleapis.com/index.html
驱动异常问题解决方案:https://blog.csdn.net/SKY_PLA/article/details/123662640

Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

配置环境变量
Path:驱动存放路径

官方文档
https://selenium-python-zh.readthedocs.io/en/latest/
'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   #导入驱动
driver.get("https://www.baidu.com")  #加载网页
####   新版本的 webdriver不在兼容使用 find_element_by_id  等方法 https://blog.csdn.net/qq_43985140/article/details/126847603
input=driver.find_element(By.ID,'kw')  #获取搜索框
input.send_keys("https://github.com/yblysyl/python_study")

button = driver.find_element(By.ID,'su')  #获取搜索按钮
print(button)
button.click()



#获取请求链接
print(driver.current_url)
#获取 cookies
print(driver.get_cookies())
#获取源代码
#print(driver.page_source)

'''
By.:
ID = "id"
XPATH = "xpath"     ###xpath 获取表单:1. "/html/body/form[1]" 2.  "//form[1]" 3. "//form[@id='loginForm']"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
'''