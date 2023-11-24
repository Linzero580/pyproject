import re

# re.search()  在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
match = re.search(r'[1-9]\d{5}', 'BIT 516500')
if match:
    # print(match.group(0))
    pass

# re.match()  从一个字符串的开始位置起匹配正则表达式，返回match对象
match = re.match(r'[1-9]\d{5}', '516500 BIT')
if match:
    # print(match.group(0))
    pass

# re.findall()  搜索字符串，以列表类型返回全部能匹配的子串
ls = re.findall(r'[1-9]\d{5}', 'BIT516500 TSU510000')
print(ls)

# re.split()  将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
ls1 = re.split(r'[1-9]\d{5}', 'BIT516500 TSU510000', maxsplit=1)
print(ls1)

# re.finditer()  搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
for ls2 in re.finditer(r'[1-9]\d{5}', 'BIT516500 TSU510000'):
    if ls2:
        print(ls2.group(0))

# re.sub()  在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
ls3 = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT516500 TSU510000')
print(ls3)
