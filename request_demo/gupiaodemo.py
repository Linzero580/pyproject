import re
import requests
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('访问失败')


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)  # 获得页面
    soup = BeautifulSoup(html, 'html.parser')  # 解析页面
    a = soup.find_all('a')  # 找到a标签
    for i in a:  # 对a标签遍历，进行处理
        try:
            href = i.attrs['href']  # 找到a标签的href属性，并判断属性中间的连接，把链接后面的数字拿出
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count=0 # 进度条初始值
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')  # 解析页面
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})  # 搜索标签找到股票所存在的大标签信息
            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            keylist = stockInfo.find_all('dt')
            valuelist = stockInfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                infoDict[key]=val

            with open(fpath, 'a', encoding='utf-8') as f :
                f.write(str(infoDict)+'\n')
                count=count+1
                print('\r当前进度：{.2f}%'.format(count*100/len(lst)),end='')
        except:
            # traceback.print_exc()
            count = count + 1
            print('\r当前进度：{.2f}%'.format(count * 100 / len(lst)), end='')
            continue


def main():
    stock_list_url = 'https://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gushitong.baidu.com/'
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


main()
