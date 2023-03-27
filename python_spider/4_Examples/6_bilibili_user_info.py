# -*-coding:utf8-*-

import requests
import json
import random
import sys
import datetime
import time
from importlib  import reload
from multiprocessing.dummy import Pool as ThreadPool
'''
###本程序的核心是以下三个api可获取bilibili对应mid=521400的个人信息
'https://api.bilibili.com/x/relation/stat?vmid=521400&jsonp=jsonp'
'https://api.bilibili.com/x/space/upstat?mid=521400&jsonp=jsonp'
'https://api.bilibili.com/x/space/acc/info?mid=521400&jsonp=jsonp'  ###本次用的是这个


###注意
1、修改cookie
2、bilibili会ip检测，多次访问后会被封ip，不影响看视频，推荐使用ip代理池：
proxie = { 
        'http' : 'http://xx.xxx.xxx.xxx:xxxx',
        'http' : 'http://xxx.xx.xx.xxx:xxx',
    }  
response = requests.get(url,proxies=proxie)

获取代理IP可参考以下项目:
https://github.com/Python3WebSpider/ProxyPool
'''
reload(sys)
time1 = time.time()
mids = []
# 设置要获取mids的范围 可自己修改这段代码  bilibili的mid是从1开始递增的 最大已知道358935649有，更大数量级或者4亿目前没有
def get_mids():
    for m in range(5214, 5215):
        for i in range(m * 100, (m + 1) * 100):
            mid = str(i)
            mids.append(mid)

def getsource(mid):

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        ###换成自己的
        'Cookie' : "buvid3=8578E581-9129-45F3-ABC1-0CBBDE15822A167610infoc; LIVE_BUVID=AUTO8116336144309302; i-wanna-go-back=-1; buvid4=C91EA00A-4DC6-0C79-AE9F-1FFDBAE74B9982679-022012117-7zkoNYWxgt8HRqCrk7Mn1g%3D%3D; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; hit-dyn-v2=1; nostalgia_conf=2; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_8578E581%22%3A%22182B0D30477%22%2C%22444.41.fp.risk_8578E581%22%3A%2218221015B4B%22%2C%22333.788.fp.risk_8578E581%22%3A%22181EB876BFF%22%2C%22333.999.fp.risk_8578E581%22%3A%22181999CAF97%22%2C%22333.881.fp.risk_8578E581%22%3A%221829A1BFC28%22%2C%22333.824.fp.risk_8578E581%22%3A%221818ADEC76B%22%2C%22888.64348.fp.risk_8578E581%22%3A%22180D535B85B%22%2C%22333.337.fp.risk_8578E581%22%3A%22181A01BFE27%22%2C%22888.2421.fp.risk_8578E581%22%3A%2218190353683%22%2C%22777.5.0.0.fp.risk_8578E581%22%3A%2218150BEE677%22%2C%22444.8.fp.risk_8578E581%22%3A%221818BB6AA85%22%2C%22666.25.fp.risk_8578E581%22%3A%22182B9D63221%22%2C%22333.874.fp.risk_8578E581%22%3A%22180F4972D17%22%2C%22444.42.fp.risk_8578E581%22%3A%221816F69237C%22%2C%22333.937.fp.risk_8578E581%22%3A%221810528B1DD%22%2C%22888.65464.fp.risk_8578E581%22%3A%221812CB6D9AF%22%2C%22888.66492.fp.risk_8578E581%22%3A%2218137130D5A%22%2C%22333.42.fp.risk_8578E581%22%3A%22181371371ED%22%2C%22666.7.fp.risk_8578E581%22%3A%221814860D594%22%7D%7D; fingerprint3=a813a039ab1e26103cb322639195a5b6; _uuid=D92BEC105-546D-102103-10D36-251E4CD3110CA95982infoc; is-2022-channel=1; b_nut=100; blackside_state=1; rpdid=|(k|mYukllll0J'uYY)Y)uR)R; ogv_channel_version=v2; PVID=1; bsource_origin=douban; hit-new-style-dyn=1; fingerprint=1bfb955e2f0fcce56478291ca4da3df0; bsource=search_bing; CURRENT_FNVAL=4048; CURRENT_PID=10bb3eb0-c8a1-11ed-a12c-cf9364221667; CURRENT_QUALITY=116; theme_style=light; home_feed_column=5; bp_video_offset_44508013=777334534698959000; b_lsid=D73DA6F7_18722DBD6FE; header_theme_version=CLOSE; sid=81h8os4o; buvid_fp=1bfb955e2f0fcce56478291ca4da3df0; innersign=0; b_ut=7"
    }
    try:
        jscontent = requests \
        .session() \
        .get('https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % mid,
            headers=head
            ) \
        .text  
        # print(jscontent)
    except Exception as e:
        print(e)
    try:
        jsDict = json.loads(jscontent)
        status_code = jsDict['code'] if 'code' in jsDict.keys() else False
        if status_code == 0:
            if 'data' in jsDict.keys():
                jsData = jsDict['data']
                mid = jsData['mid']
                name = jsData['name']
                sex = jsData['sex']
                rank = jsData['rank']
                face = jsData['face']
                regtimestamp = jsData['jointime']
                regtime_local = time.localtime(regtimestamp)
                regtime = time.strftime("%Y-%m-%d %H:%M:%S", regtime_local)
                
                birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'nobirthday'
                sign = jsData['sign']
                level = jsData['level']
                OfficialVerifyType = jsData['official']['type']
                OfficialVerifyDesc = jsData['official']['desc']
                vipType = jsData['vip']['type']
                vipStatus = jsData['vip']['status']
                coins = jsData['coins']
                print("mid:",mid,"name:",name,"sex:",sex,"rank:",rank,"face:",face,"regtimestamp:",regtimestamp,
                        "regtime_local:",regtime_local,"regtime:",regtime,"birthday:",birthday,"sign:",sign,"level:",level,"OfficialVerifyType:",OfficialVerifyType,
                        
                        "OfficialVerifyDesc:",OfficialVerifyDesc,"vipType:",vipType,"vipStatus:",vipStatus,"coins:",coins)
            else:
                print('no data now')
        else:
            print("Error: " + mid)
    except Exception as e:
        print(e)
        pass
if __name__ == "__main__":
    get_mids()
    pool = ThreadPool(1)
    try:
        results = pool.map(getsource, mids)
    except Exception as e:
        print(e)
    pool.close()
    pool.join()
