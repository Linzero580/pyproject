import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
r.encoding = r.apparent_encoding
demo = r.text
print(demo)
# print('---------------------------------')
soup = BeautifulSoup(demo, 'html.parser')
print('---------------------------------')
# print(soup.find(name='b').parent)
print('---------------------------------')
print(soup.find(attrs={'py1'}).previous_sibling)
print('---------------------------------')
for i in soup.find(attrs={'py1'}).next_siblings:
    print(i)