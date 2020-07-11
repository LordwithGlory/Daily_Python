import requests
from bs4 import BeautifulSoup
import urllib
import os
import time

def findone(url,base_url):
    strhtml=requests.get(url)
    # 解决编码问题
    strhtml.encoding='utf-8'
    # print(strhtml.text)
    next_url=None
    htmltext=strhtml.text
    # 解析网页信息
    soup=BeautifulSoup(htmltext,'html.parser',fromEncoding="utf-8")
    # 设置xls存储路径
    if not os.path.exists('./datas/'):
        os.mkdir('./datas/')
    links=soup.find_all('a')
    # 遍历所有连接
    for link in links:
        # 是文件则存储
        file_url=base_url+link['href']
        if 'xls' in link['href']:
            print('downloading '+link.get_text())
            urllib.request.urlretrieve(file_url,'./datas/'+link.get_text()+'.xls')
        elif 'pdf' in link['href']:
            print('downloading '+link.get_text())
            urllib.request.urlretrieve(file_url,'./datas/'+link.get_text()+'.pdf')
        # 获取下一页连接
        if link.get_text()=='下一页':
            next_url=base_url+link['href']
    return next_url

base_url='http://www.csf.com.cn'
url='http://www.csf.com.cn/publish/main/1022/1024/1127/index.html'
nexturl=findone(url,base_url)
# 一直进行下载
while nexturl is not None:
    if url==nexturl:
        print("下载完成")
        break
    url=nexturl
    nexturl=findone(url,base_url)
    time.sleep(1)
    print(nexturl)