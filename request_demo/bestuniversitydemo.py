import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLtxt(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 检测tr标签的类型，不是bs库的tag，就过滤掉
            tds = tr('td')
            # print(tds)
            # print('------------------------------')
            ulist.append([tds[0].string.strip(), tds[1].find('a').string.strip(), tds[2].text.strip()])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "省份", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []  # 将信息放在一个列表中
    url = "https://www.shanghairanking.cn/rankings/bcur/2023"
    html = getHTMLtxt(url)  # 将url转换成html格式
    fillUnivList(uinfo, html)  # 将html的信息提取后放在uinfo中
    printUnivList(uinfo, 10)  # 输出前20


main()
