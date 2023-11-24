import os.path

import requests
#
# url='https://origin-www.amazon.cn/dp/B003JK8SUW?ref_=Oct_DLandingS_D_a3ff8d7e_14&th=1'
# r=requests.get(url)
# print(r.request.headers)
# print(r.status_code)
# print(r.text)
# print(r.encoding)

url='https://img0.baidu.com/it/u=1479424396,1021876073&fm=253&fmt=auto&app=138&f=JPEG?w=567&h=482.jpg'
root='D://testpics//'
path=root+url.split('=')[-1] # split,按照规则分割url,取list最后一个值当文件名
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件保存失败')
except:
    print('访问失败')
