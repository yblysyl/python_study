import requests

headers = {
    # 假装自己是浏览器    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': 'eda38d470a662ef3606390ac3b84b86f9; Hm_lvt_f1d3b035c559e31c390733e79e080736=1553503899; biihu__user_login=omvZVatKKSlcXbJGmXXew9BmqediJ4lzNoYGzLQjTR%2Fjw1wOz3o4lIacanmcNncX1PsRne5tXpE9r1sqrkdhAYQrugGVfaBICYp8BAQ7yBKnMpAwicq7pZgQ2pg38ZzFyEZVUvOvFHYj3cChZFEWqQ%3D%3D; Hm_lpvt_f1d3b035c559e31c390733e79e080736=1553505597',
}

session = requests.Session()
response = session.get('https://github.com/yblysyl/python_study', headers=headers)

print(response.text)

'''
第一种最简单是用表单包含用户名密码去请求
第二种用cookie
第三种用selenium 模拟登录
'''
####范例未经测试
from selenium.webdriver.support.ui import WebDriverWait  #from selenium.webdriver.support.wait import WebDriverWait 等待
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
browser = webdriver.Chrome()
WAIT = WebDriverWait(browser, 10)
username = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "帐号的selector")))
password = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "密码的selector")))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '按钮的xpath')))
username.send_keys('你的帐号')
password.send_keys('你的密码')
submit.click()
cookies = webdriver.get_cookies()
