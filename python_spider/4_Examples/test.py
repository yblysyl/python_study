from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
import re
import os
import xlwt ##写入excel
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  #from selenium.webdriver.support.wait import WebDriverWait 等待
from selenium.webdriver.support import expected_conditions as EC

####系统配置
driver = webdriver.Chrome()   #导入驱动
#driver2 = webdriver.Chrome()
page_num=30  ### 设置百度查询页数

##打开excel
key_Search='新冠'   ##要搜集信息的关键词
#filename='鸡你太美'  ##存储的文件名
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheet = book.add_sheet(filename, cell_overwrite_ok=True)
# sheet.write(0, 0, 'url')
# sheet.write(0, 1, '文本')
# n = 1 ##excel表格行数信息

##解析页面信息
def get_source():
    time.sleep(3)
    html = driver.page_source
    #解析html
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a')
    linkall=[]
    for link in links:
         real_url=get_real_url(link.get('href'))
         if url_get(real_url)!=1 :
                continue
         linkall.append(link.get('href'))
    print(linkall)
    # # 获取页面所有文本
    texts = soup.find('body').text
    chinese_text = re.findall('[\u4e00-\u9fff]+', texts)
    chinese_text2 = [re.sub('[^\u4e00-\u9fff]+', '', text) for text in chinese_text]
    print(chinese_text2)
        
        
### requests.get(url) 状态码 200返回1 其他返回0  错误返回2  判断url对于request是否可用
def url_get(url):
    try:
       r = requests.get(url) 
       if(r.status_code==200):
           return 1
       else:
           return 0
    except Exception as e:
        return 2
#初始化配置 进入百度页面
def main():
    driver.get("https://www.baidu.com")  #加载网页
    input=driver.find_element(By.ID,'kw')  #获取搜索框
    input.send_keys(key_Search)
    button = driver.find_element(By.ID,'su')  #获取搜索按钮
    button.click()
    ##开是获取查询的每页信息
    active_btn=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"page-inner_2jZi2").find_element(By.TAG_NAME,'strong'))
    print(active_btn.text)
    page_start(1)

###页面校验和下一页跳转
def page_start(sum):
    try:
        sume=sum
        active_btn=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"page-inner_2jZi2").find_element(By.TAG_NAME,'strong'))
        print(active_btn.txt)
        while True:
            time.sleep(3)
            print(sume)
            try:
                active_btn=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"page-inner_2jZi2").find_element(By.TAG_NAME,'strong'))
                print(active_btn.txt)
            except Exception:
                print('获取页数信息出错')
                continue
            global page_num
            if int(active_btn.text)>page_num:##运行结束
                return
            if int(active_btn.text)==sume:##运行正常
                print('获取第'+str(sume)+'页数据:')
                get_source()
                page_start(sume+1)
                continue
            elif int(active_btn.text)<sume:
                try:
                    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,'n'))
                    next_btn=driver.find_elements(By.CLASS_NAME,'n')[0]  #获取下一页按钮
                    next_btn.click()
                    continue
                except Exception:
                    print('下一页异常')
                    continue
            elif int(active_btn.text)>sume:
                sume=sume+1
    except Exception:
        print('翻页出错')
        page_start(sume)
        # driver.refresh()
        
        # return next_page(page_num)



##解析百度地址--获取真实地址
def get_real_url(v_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Host": "www.baidu.com",
        # 需要更换Cookie
        "Cookie": '__yjs_duid=1_7b49fc15e97b98aa88409cc07e63da5b1633405212352; BIDUPSID=F5FC69633DB6AD42FDBC17CB38EA24EC; PSTM=1633405212; BDSFRCVID=h3LOJexroG0RT0bDD7DqMHDFRgKK0gOTDYLEOwXPsp3LGJLVgxPTEG0PtjJ5HU4bLrA9ogKKBgOTH4FF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI0aJDvDqTrP-trf5DCShUFsbPKJB2Q-XPoO3KJWePOPQhjEyPFAQfTLtpTPQRnt_fbgy4op8P3y0bb2DUA1y4vpK55Da2TxoUJ2bUOJfxjJqtnWeMLebPRi3tb9Qg-JKqQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD5thj6PVKgTa54cbb4o2WbCQ3p7r8pcN2b5oQT8bbpba0p50J6RPKRrEJUclSDbGjlOUWJDkXpJvQnJjt2JxaqRC5KQaDp5jDh3M5hts5RQme4ROfgTy0hvc0J3cShPmQxjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT-tJJ3aQ5rtKRTffjrnhPF3efC0XP6-hnjy3bRO0-Ot3UQhsDnaQtTVjhIA3HOttq3Ry6r42-39LPO2hpRjyxv4bTKLhPoxJpOJbN7MLfjnHR7Wbh5vbURvL4-g3-AJ0f5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoD8MJD-5hI0r-R-_-4_tbh_X5-RLf5r0_p7F54nKDp0x0l82-x0v2-ouWxvR3HrMahkM5h7xsMTsQfnbWh8yKabr0MTrQDvObUbN3KJmfbc_jf7lj-DTK4L82-biW2rM2MbdJpQP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6K5D553DN-fq-jeHDrKBRbaHJOoDDvdDUvcy4LbKxnxJpjntIrRKI3g-l61shQ-bURvD--g3-OkWUQ9babTQ-tbBp3k8MQT2h3xQfbQ0hOBBjQ7QRna2PopfR7JOpvtbUnxy50zQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IKKJKQP; H_WISE_SIDS_BFESS=110085_127969_176398_179346_182234_184012_184286_184440_185268_186841_187392_187726_188453_188553_188747_188874_189731_189755_189975_190146_190473_190622_190683_190796_191067_191369_191810_192011_192206_192351_192407_192672_192958_193042_193283_193558_193635_193756_193882_194085_194514_194519_194583_194672_195155_195175_195189_195343_195477_195543_195551_195591_195678_195839_196001_196045_196051_196230_196275_196426_196489_196591_196701_196754_196833_196847_196940_197001_197027_197147_197215_197221_197241_197288_197469_197668_197710_197783_197829_198033_198181_198242_198255_198312_198429_198446_198510_198876_198902_198928; BDUSS=ptSm9oek5KNzFyckNlV3BGVm5CMkVJT2RIZnBRb35ySWdIY0ljSG42NXFWMWRqRVFBQUFBJCQAAAAAAAAAAAEAAAB3YsSO09p5dWJsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGrKL2Nqyi9jSm; BDUSS_BFESS=ptSm9oek5KNzFyckNlV3BGVm5CMkVJT2RIZnBRb35ySWdIY0ljSG42NXFWMWRqRVFBQUFBJCQAAAAAAAAAAAEAAAB3YsSO09p5dWJsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGrKL2Nqyi9jSm; BAIDUID=8DC2797D22188D4D5D0E185554D8133E:FG=1; MCITY=-301:; BD_UPN=12314753; BDSFRCVID_BFESS=h3LOJexroG0RT0bDD7DqMHDFRgKK0gOTDYLEOwXPsp3LGJLVgxPTEG0PtjJ5HU4bLrA9ogKKBgOTH4FF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oI0aJDvDqTrP-trf5DCShUFsbPKJB2Q-XPoO3KJWePOPQhjEyPFAQfTLtpTPQRnt_fbgy4op8P3y0bb2DUA1y4vpK55Da2TxoUJ2bUOJfxjJqtnWeMLebPRi3tb9Qg-JKqQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD5thj6PVKgTa54cbb4o2WbCQ3p7r8pcN2b5oQT8bbpba0p50J6RPKRrEJUclSDbGjlOUWJDkXpJvQnJjt2JxaqRC5KQaDp5jDh3M5hts5RQme4ROfgTy0hvc0J3cShPmQxjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT-tJJ3aQ5rtKRTffjrnhPF3efC0XP6-hnjy3bRO0-Ot3UQhsDnaQtTVjhIA3HOttq3Ry6r42-39LPO2hpRjyxv4bTKLhPoxJpOJbN7MLfjnHR7Wbh5vbURvL4-g3-AJ0f5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoD8MJD-5hI0r-R-_-4_tbh_X5-RLf5r0_p7F54nKDp0x0l82-x0v2-ouWxvR3HrMahkM5h7xsMTsQfnbWh8yKabr0MTrQDvObUbN3KJmfbc_jf7lj-DTK4L82-biW2rM2MbdJpQP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6K5D553DN-fq-jeHDrKBRbaHJOoDDvdDUvcy4LbKxnxJpjntIrRKI3g-l61shQ-bURvD--g3-OkWUQ9babTQ-tbBp3k8MQT2h3xQfbQ0hOBBjQ7QRna2PopfR7JOpvtbUnxy50zQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IKKJKQP; ispeed_lsm=2; BD_HOME=1; BD_CK_SAM=1; PSINO=1; delPer=0; BA_HECTOR=al00052g81810ha4ag8h210u1i1vr731m; BAIDUID_BFESS=8DC2797D22188D4D5D0E185554D8133E:FG=1; ZFY=xWfWeO2SFe18S9HUVHb7LIRz2C5:A1CFaj7AaogtvT6U:C; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; B64_BOT=1; H_PS_PSSID=38185_36552_38359_38468_38173_38290_38375_37933_38343_37900_26350_38419_38282_37881; baikeVisitId=f617168d-1433-41b3-ac67-1630430ed1ad; RT="z=1&dm=baidu.com&si=f61158db-79bb-4f93-a08a-e2b503a11f7e&ss=lfp2rcq8&sl=1&tt=3lr&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=4eh"; H_PS_645EC=be74WiwNjxi3T3TXASHd4B94uztc699kK4d6/qRxBYOUVif969oXW6qFjabw+OxdX/DK'
    } 
    try:
        r = requests.get(v_url, headers=headers, allow_redirects=False)  # 不允许重定向
        if r.status_code == 302:  # 如果返回302，就从响应头获取真实地址
            real_url = r.headers.get('Location')
        else:  # 否则从返回内容中用正则表达式提取出来真实地址
            real_url = re.findall("URL='(.*?)'", r.text)[0]
        return real_url
    except Exception as e:
        return "地址错误"

##主方法
if __name__ == '__main__':
    main()
