#selenium + phantomjs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  #from selenium.webdriver.support.wait import WebDriverWait 等待
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os
import xlwt ##写入excel

'''
又一个教程:该教程没有语言倾向各种语言都有范例
https://www.selenium.dev/zh-cn/documentation/webdriver/

该页面基本采用
https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/windows/
中的代码
'''

key_Search='鸡你太美'   ##要搜集信息的关键词
filename='鸡你太美'  ##存储的文件名


# browser = webdriver.PhantomJS()
##打开窗口
browser = webdriver.Chrome()
WAIT = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)

##打开excel
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet(filename, cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '地址')
sheet.write(0, 2, '作者')
sheet.write(0, 3, '发布时间')
sheet.write(0, 4, '播放量')
sheet.write(0, 5, '弹幕数量')
n = 1 ##excel表格行数信息
end=False
def search():
    try:
        print('开始访问b站....')
        browser.get("https://www.bilibili.com/")
        input = WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input")))   ###注意前端页面变化会导致脚本失效  --要及时适配
        submit = WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-search-btn")))
        input.send_keys(key_Search) ##修改此处修改
        submit.click()
        # 跳转到新的窗口
        print('跳转到新窗口')
        all_h = browser.window_handles
        browser.switch_to.window(all_h[1])
        get_source()
        next_page(1)##开始页面切换，页面切换用了递归
    except TimeoutException:
        return search()


def next_page(page_num):
    try:
        print('获取下一页数据',page_num)
        print(browser.current_url)
        WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,'vui_pagenation--btn-side'))
        next_btn=browser.find_elements(By.CLASS_NAME,'vui_pagenation--btn-side')[1]  #获取下一页按钮
        print(next_btn.text)
        next_btn.click()
        active_btn=WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"vui_button--active-blue"))##获取当前页信息
        ##以下为逻辑校验，校验是否结束；是否数据正确
        if int(active_btn.text)==page_num:
            get_source()
            next_page(page_num+1)
        elif int(active_btn.text)>page_num:
            get_source()
            next_page(page_num+2)
        else :
            return
    except TimeoutException:
        browser.refresh()
        return next_page(page_num)


def save_to_excel(soup):
    list = soup.find(class_='video-list').find_all(class_='bili-video-card__wrap __scale-wrap')
    # time.sleep(1000)
    for item in list:
        item_title = item.find('img').get('alt')
        item_link = item.find('a').get('href')
        item_author= item.find(class_='bili-video-card__info--author').text   
        item_date= item.find(class_='bili-video-card__info--date').text 
        item_bf= item.find(class_='bili-video-card__stats--left').find_all('span')
        item_bf1=item_bf[1].text
        item_bf2=item_bf[3].text
        item_datetime= item.find(class_='bili-video-card__stats__duration').text 
        print('爬取：' + item_title+'|'+item_link+'|'+item_author+'|'+item_date+'|'+item_bf1+'|'+item_bf2+'|'+item_datetime)
        global n
        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_author)
        sheet.write(n, 3, item_date)
        sheet.write(n, 4, item_bf1)
        sheet.write(n, 5, item_bf2)
        sheet.write(n, 6, item_datetime)
        n = n + 1
        global filename
        book.save(os.path.dirname(os.path.abspath(__file__))+'\\bilibili_search_info\\'+filename+'.xls')
    # time.sleep(1000)

def get_source():
    html = browser.page_source
    #解析html
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


def main():
    try:
        search() ###初始化
    finally:
        browser.close()
##主方法
if __name__ == '__main__':
    main()