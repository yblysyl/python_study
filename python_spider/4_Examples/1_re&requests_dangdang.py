import requests
import re
import json
import os
'''
该项目爬取当当网 http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1 页面中罗列的数据信息
主要练习 正则表达式的使用 次要练习 requests

'''
##保存信息 注意路径----- python的路径是相对于你当前打开文件夹的相对路径  如果直接运行则是相对项目目录
def write_item_to_file(item):
   print('开始写入数据 ====> ' + str(item))
   
   '''
   这段代码的作用是打印出当前工作目录，以及当前文件的绝对路径和规范路径。
   os.getcwd()返回当前工作目录的路径名
   os.path.abspath(__file__)返回当前文件的绝对路径
   os.path.realpath(__file__)返回当前文件的规范路径。
   os.path.dirname()返回指定路径名的父目录名。
   os.path.dirname(os.path.abspath(__file__))来获取当前文件所在的文件夹路径。
   '''
   ##with open('python_spider/4_Examples/book.text', 'a', encoding='UTF-8') as f:
   with open(os.path.dirname(os.path.abspath(__file__))+'\\book.text', 'a', encoding='UTF-8') as f:
       f.write(json.dumps(item, ensure_ascii=False) + '\n')
       f.close()

##操作主体
def main(page):
   ##设计url格式
   url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
   html = request_dandan(url) #连接url
   items = parse_result(html) # 解析html信息
   end=0 ###判断是否已经没有数据，若有继续递归调用方法
   for item in items:
       end=end+1
       write_item_to_file(item) #保存信息
       #print(item)
   if end!=0:
      main(page+1)
       
    #连接url方法 并作异常处理   
def request_dandan(url):
   try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None
###解析html获取主要数据
def parse_result(html):
   pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">&yen;(.*?)</span>.*?</li>',re.S)
   #print(re.findall('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name',html,re.S))
   #print(re.findall('class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>',html,re.S))
   #print(re.findall('</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng"',html,re.S))
   #print(re.findall('class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">&yen;(.*?)</span>.*?</li>',html,re.S))
   
   
   '''
   关于yield与生成器generator的关系
   
   方法中带有 yield关键字的函数 返回值为 generator 。
   函数是顺序执行的,遇到return语句或者最后一行函数语句就返回
   变成generator的函数,在每次调用next()的时候执行,遇到yield语句返回,再次被next()调用的时候就从上次的返回yield语句处继续执行。
   
   '''
   items = re.findall(pattern,html)   
   for item in items:
       yield {
           'range': item[0],
           'iamge': item[1],
           'title': item[2],
           'recommend': item[3],
           'author': item[4],
           'times': item[5],
           'price': item[6]
       }


#主方法
if __name__ == "__main__":
   main(1)