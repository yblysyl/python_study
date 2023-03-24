
import requests
'''
Requests 是在 urllib 的基础上搞出来的
通过它我们可以用更少的代码
模拟浏览器操作
'''


#Get 请求
r = requests.get('https://api.github.com/events')
print(r)
print("#######################################################################################")
# Post 请求
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r)
print("#######################################################################################")
'''
其它乱七八糟的 Http 请求
>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('https://httpbin.org/delete')
>>> r = requests.head('https://httpbin.org/get')
>>> r = requests.options('https://httpbin.org/get')
'''

#携带请求参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r)
print("#######################################################################################")

#伪装浏览器
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r)
print("#######################################################################################")

#获取服务器响应文本内容
import requests
r = requests.get('https://api.github.com/events')
print(r.text)#输出为文本
print(r.encoding)#输出编码 utf-8
print(r.content)#获取字节响应内容
print(r.status_code) #获取响应码
print("#######################################################################################")
print(r.headers) #获取响应头
print("#######################################################################################")
r = requests.get('https://api.github.com/events')
print(r.json()) #获取 Json 响应内容
print("#######################################################################################")
#获取 socket 流响应内容
r = requests.get('https://api.github.com/events', stream=True)
r.raw
r.raw.read(10)
print("#######################################################################################")
#Post请求 一个键添加多个值
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
print(r2.text)    #######y有问题r2应该有值 出现错误
print(r1.text == r2.text)
print("#######################################################################################")
#请求的时候用 json 作为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r.text)
print("#######################################################################################json 作为参数")

#上传文件   注意路径容易出错
url = 'https://httpbin.org/post'
files = {'file': open('python_spider/requests_study/report.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)
print("#######################################################################################上传文件")


#获取 cookie 信息
''' 运行出错
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies['example_cookie_name'])
print("#######################################################################################获取 cookie 信息")
'''

#发送 cookie 信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
print("########################################################################################发送 cookie 信息")


#设置超时  --报错是正常的 效果如此
requests.get('https://github.com/', timeout=0.001)
print("########################################################################################设置超时")