import requests, xlwt, sys
from lxml import etree
import lxml
import time


"""
# File: test.py
# Written by JessyTsui
# Time: 2021/10/3 11:45 下午
# IDE: PyCharm
# Have a good day！
"""

# def spider():
# url = "https://school.wjszx.com.cn/senior/introduce-1.html"

time_start = time.time() #开始计时

for i in range(1,1000):
    url = "https://school.wjszx.com.cn/senior/introduce-{}.html".format(i)
    html = requests.get(url)
    html.encoding = "utf-8"
    selecter = etree.HTML(html.text)
    name = '//h1/text()'
    Time = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/@title'
    phone = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/@title'
    address = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/@title'
    url = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[4]/@title'
    name = selecter.xpath(name)
    Time = selecter.xpath(Time)
    phone = selecter.xpath(phone)
    address = selecter.xpath(address)
    url = selecter.xpath(url)

    name = ''.join(name)
    Time = ''.join(Time)
    phone = ''.join(phone)
    address = ''.join(address)
    url = ''.join(url)

    fo = open('1.txt', 'a')  # a表示追加写
    fo.write(name + '+' + Time + '+' + phone + '+' + address + '+' + url)
    fo.write(' \n')
    fo.close()
    print(name+' 抓取成功 ')

print("一共抓取1000个")
time_end = time.time()  # 结束计时
time_c = time_end - time_start  # 运行所花时间
print('用时', time_c, 's')
