import re
'''
https://blog.csdn.net/weixin_62651706/article/details/126123839
https://blog.csdn.net/zaf0516/article/details/122734231
'''
#?	该修饰符用于其它修饰符后面，表示匹配模式为非贪婪的 
content = "Xiaoshuaib has 100 bananas"
print(re.match('^Xi.*(\d+).*s$',content).group(1),re.match('^Xi.*?(\d+).*s$',content).group(1))
#匹配将对左边正则中的每个()进行匹配并返回类似数组用group访问
content = 'Xiaoshuaib has 1000 bananas'
res = re.match('^.*(10(0)).*$',content)
print(res.group(0)+','+res.group(1)+','+res.group(2)+',')

#全匹配
print(re.match('.*',"test").group(0))


#搜索所有匹配子串返回列表
import re
print(re.findall('se*',"testdadwaseeawdwsedwasdase"))
#搜索所有匹配子串返回迭代器
print(re.finditer('se*',"testdadwaseeawdwsedwasdase"))

#替换字符串
print(re.sub('se*',"yubinlei","testdadwaseeawdwsedwasdase"))
#切片
print(re.split(',','yu,bin,lei'))


#re.pattern
#re.flags





