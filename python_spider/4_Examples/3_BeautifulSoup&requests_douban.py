import requests
import xlwt
import os
from bs4 import BeautifulSoup
'''
豆瓣 top250网站信息获取
https://movie.douban.com/top250

requests负责访问
BeautifulSoup负责解析
xlwt负责写入excel
os负责路径定位
'''
def main(page):
   url = 'https://movie.douban.com/top250?start=' + str(page*25)+'&filter='
   global n ##引入外部变量声明
   html = request_douban(url)  #获取html
   soup = BeautifulSoup(html, 'lxml') #解析html
   list = soup.find(class_='grid_view').find_all('li')
   for item in list:
       item_name = item.find(class_='title').string  # 电影名 find只能获取到第一个元素
       item_a = item.find('a').get('href')  # 该电影详情页
       item_img = item.find('a').find('img').get('src')  # 图片地址
       item_index = item.find(class_='').string  # 获取排名索引
       item_score = item.find(class_='rating_num').string  # 评分
       item_author = item.find('p').text  # 导演 地区 风格
      # item_intr = item.find(class_='inq').string  ##一句吸引人的话
       try:
           item_intr = item.find(class_='inq').text  ##一句吸引人的话
       except Exception:
           item_intr="无"
       print('爬取电影：' + item_index + ' | ' + item_name )
       sheet.write(n, 0, item_name)####写入excel
       sheet.write(n, 1, item_index)
       sheet.write(n, 2, item_score)
       sheet.write(n, 3, item_author)
       sheet.write(n, 4, item_intr)
       sheet.write(n, 5, item_img)
       sheet.write(n, 6, item_a)
       n=n+1
def request_douban(url):
   try:
       # 伪装浏览器 user-agent内容在浏览器network中能找到   不伪装则报418错
       headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
       response = requests.get(url,headers=headers)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None
book = xlwt.Workbook()
#新建表格，写入头。由此可见python的全局变量定义位置和使用的上下位置无关，只要在执行到使用前定义即可。
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '排名')
sheet.write(0, 2, '评分')
sheet.write(0, 3, '作者')
sheet.write(0, 4, '简介')
sheet.write(0, 5, '图片')
sheet.write(0, 6, '详情页')
n = 1

for i in range(0, 10):
       main(i)
##将内存中的信息保存到同级项目目录
book.save(os.path.dirname(os.path.abspath(__file__))+'\\豆瓣最受欢迎的250部电影.xls')