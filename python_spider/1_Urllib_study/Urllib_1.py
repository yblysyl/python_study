import urllib.request

'''Python内置的 Urllib 库中有 4 个模块
request:
request模块用的比较多用它来发起请求
error:
当我们在使用 request 模块遇到错误用它来进行异常处理
parse:
p用来解析我们的 URL 地址的,比如解析域名地址、URL指定的目录等
robotparser:
用的就比较少，用来解析网站的 robot.txt
'''
#访问url并返回结果
#urllib.request.urlopen(url, data=None, [timeout, ]*)  url 就是我们请求的链接 data 就是专门给我们 post 请求携带参数的 timeout 就是设置请求超时时间
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
#urllib.request.Request(url, data=None, headers={}, method=None)

