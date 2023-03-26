import requests
import re
import json
import os

#https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=2020%E5%B9%B4%E6%98%A5%E8%8A%82%E6%A1%A3%E7%94%B5%E5%BD%B1&oq=2020%25E5%25B9%25B4%25E6%2598%25A5%25E8%258A%2582&rsv_pq=a1a6ac19002546da&rsv_t=bec7NKQ53jAT5fegf8z5fffiZ9fwTMPkkhJTi3VBmPGllwbfeK%2F2%2FeNIrp4&rqlang=cn&rsv_enter=1&rsv_dl=ts_3&rsv_btype=t&rsv_sug3=33&rsv_sug1=20&rsv_sug7=100&rsv_sug2=1&prefixsug=2020%25E5%25B9%25B4%25E6%2598%25A5%25E8%258A%2582&rsp=3&rsv_sug4=1294
'''
 https://www.baidu.com/s?wd=%E6%96%B0%E9%A6%86%E7%96%AB%E6%83%85&rsv_spt=1&rsv_iqid=0x81ca21a1001b38c9&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=%25E6%2596%25B0%25E5%2586%25A0%25E7%2596%25AB%25E6%2583%2585&rsv_btype=t&rsv_t=ed9b2TAtTPOm8Ku%2F%2BRDbmwcdsTao%2FyPSKheBnOPSkpi2Xa4BZJTUJ3gD1GAJxQ8%2FYxyd&rsv_pq=91e23a0900190a50





'''
##操作主体
def main(page):
   ##设计url格式
   print(111)
   url = 'https://www.baidu.com/'
   html = request_dandan(url) #连接url
   print(html)
#    items = parse_result(html) # 解析html信息
#    end=0 ###判断是否已经没有数据，若有继续递归调用方法
#    for item in items:
#        end=end+1
#        write_item_to_file(item) #保存信息
#        #print(item)
#    if end!=0:
#       main(page+1)
       
    #连接url方法 并作异常处理   
def request_dandan(url):
   try:
       headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
       payload = {'wd': '新冠疫情', 
                  'rsv_spt': '1',
                  'ie' : 'utf-8',
                  'bs':'新冠疫情'
                  }
       print(222)
       response = requests.get(url)
       print(333)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None

#主方法
if __name__ == "__main__":
   main(1)