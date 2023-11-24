import requests

# url = 'https://detail.tmall.com/item.htm?id=592376169592'
url = 'https://item.jd.com/10084472905496.html'

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.encoding)
    print(r.text)
except:
    print('访问失败')
