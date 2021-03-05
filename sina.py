from urllib.parse import quote
import string
import urllib.request as request
from bs4 import BeautifulSoup as bs
import re
def getNews(name):
    url='https://search.sina.com.cn/?q='+name+'&c=news&from=channel'
    url_request = quote(url, safe=string.printable)  # 解决ascii编码报错问题，不报错则可以注释掉
    head = {}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                       'Chrome/88.0.4324.150 Safari/537.36'
    req=request.Request(url_request,method='GET',headers=head)
    answer=request.urlopen(req,timeout=10)
    html=answer.read().decode('utf-8')
    soup = bs(html, 'html.parser')
    title='<a href=.*? target="_blank">(.*?)</a>'
    for it in soup.find_all('div', class_="box-result clearfix"):
        # print(it)
        ti=re.findall(title,str(it))[0]
        ti=re.sub('<.*?>','',ti)
        print(ti)
    # print(html)

import time
news=['阿里巴巴','腾讯','百度']
while True:
    for new in news:
        getNews(new)
    time.sleep(60*60*3)