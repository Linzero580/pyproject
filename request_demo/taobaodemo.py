import requests
import re
from bs4 import BeautifulSoup


# 获得页面的函数
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('访问失败')


# 对页面进行解析
def parsePage(ilt, html):
    soup = BeautifulSoup(html, 'html.parser')


# 将商品信息输出
def printGoodsList(ilt):
    pass


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            continue
    printGoodsList(infolist)


main()
