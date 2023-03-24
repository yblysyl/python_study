from urllib import request,parse
import ssl

#如果网站是https要导入  --使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()
#定义我们的请求 url 和 header  
url = 'https://biihu.cc//account/ajax/login_process/'  #fiddler   右侧header内容
headers = {
    #伪装浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}


##定义请求参数  #fiddler 右侧webFroms内容
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}
#将请求的参数转化为 byte型
data = bytes(parse.urlencode(dict),'utf-8')

req = request.Request(url,data=data,headers=headers,method='POST')
response = request.urlopen(req,context=context)
print(response.read().decode('utf-8'))