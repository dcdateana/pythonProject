import urllib.request as ur,urllib.parse as up,json,time,os,urllib.error as ue
# response=ur.urlopen('http=//placekitten.com/g/500/600')
# r=response.read()
# with open('cat.jpg','wb') as f=
#     f.write(r)

# 翻译
# while True:
#     content=input('需要翻译的内容')
#     url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#
#     head={}
#     head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
#                        'Chrome/87.0.4280.141 Safari/537.36'
#     data={}
#     data['i']= content
#     data['from']= 'AUTO'
#     data['to']= 'AUTO'
#     data['smartresult']= 'dict'
#     data['client']= 'fanyideskweb'
#     data['salt']= '16123541852631'
#     data['sign']= 'b6dcffe4e76377ac4edabf0a65114650'
#     data['lts']= '1612354185263'
#     data['bv']= 'eac2bf78c46bf1bab5b4558752481e4a'
#     data['doctype']= 'json'
#     data['version']= '2.1'
#     data['keyfrom']= 'fanyi.web'
#     data['action']= 'FY_BY_CLICKBUTTION'
#     data=up.urlencode(data).encode('utf-8')
#
#     req=ur.Request(url,data,head)
#     response=ur.urlopen(req)
#     html=response.read().decode('utf-8')
#     html=json.loads(html)
#     print(html['translateResult'][0][0]['tgt'])
#     time.sleep(5)、

# bili爬取
from bs4 import BeautifulSoup as bs
import re
import xlwt
import sqlite3
import urllib.error as uerror
from io import BytesIO
import gzip
import ast


def main():
    baseurl='https://www.bilibili.com/video/BV1Fs411A7HZ'
    data=getDate(baseurl)
    print(data)
find=re.compile('"rotate":0},"no_cache":false,"pages":(.*?),"subtitle":\{"allow_submit":false,"list":\[]}')

# findlink=re.compile(r'<a href="(.*?)">')
# findImage=re.compile(r'<img alt=".*?" class="" src="(.*?)" width="100"/>')
# findName=re.compile(r'<span class="title">(.*?)</span>')
# findRate=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# findPeople=re.compile(r'<span>(\d*人评价)</span>')
# findInq=re.compile(r'<span class="inq">(.*?)</span>')
# findBd=re.compile('<p class="">\n(.*?)</p>',re.S)

def getDate(baseurl):
    head={}
    head['User-Agent']= 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    head['cookie']= "_uuid=4DF658AD-EB92-EADF-393D-EFFB83F7BDF733839infoc; " \
                    "buvid3=2B88365C-E28D-4BE6-ABA0-31FC4D9E2924138389infoc; " \
                    "sid=535jdc86; DedeUserID=34579676; " \
                    "DedeUserID__ckMd5=51fca603380fbb68; " \
                    "SESSDATA=88f78d9f%2C1614739961%2C4710b*91; " \
                    "bili_jct=687a492688070376cbec9e7e83b2392b; " \
                    "blackside_state=1; rpdid=|(k|mmmYu~R~0J'ulmmu))|||; " \
                    "LIVE_BUVID=AUTO6915994456989062; CURRENT_QUALITY=120; " \
                    "CURRENT_FNVAL=80; fingerprint3=80db24cb2e912ba76b0795aa67d3435a; " \
                    "fingerprint=f50fdbea6ff4456a6f1713c6b64cc390; " \
                    "fingerprint_s=d70195ecec9c3b2b81e7773f0567cc2b; " \
                    "buvid_fp=2B88365C-E28D-4BE6-ABA0-31FC4D9E2924138389infoc; " \
                    "buvid_fp_plain=2B88365C-E28D-4BE6-ABA0-31FC4D9E2924138389infoc; " \
                    "Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1609215600,1609415160,1611218517; " \
                    "bsource=search_baidu; finger=1571944565; " \
                    "_dfcaptcha=0c87ce54010ea076c8e68c3e4a2cda24; " \
                    "PVID=1; bp_video_offset_34579676=489716835428801867; " \
                    "bp_t_offset_34579676=489716835428801867"
    req=ur.Request(baseurl, method='GET',headers=head)
    try:
        response=ur.urlopen(req)
        html=response.read()
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode('utf-8')
        html=re.findall(find,html)
        print(html)
        # html=json.load(html[0])
        html=ast.literal_eval(html[0])
        print(html)

        for item in html:
            print(item['part'])

# 解析
#         soup=bs(html,'html.parser')
#         for item in soup.find_all('div',class_ = "item"):
#             # print(item)
#             data=[]
#             item=str(item)
#
#             link=re.findall(findlink,item)[0]
#             data.append(link)
#
#             imgSrc=re.findall(findImage,item)[0]
#             data.append(imgSrc)
#
#             name=re.findall(findName,item)
#             if len(name)==2:
#                 data.append(name[0])
#                 otitle=name[1].replace('/','')
#                 otitle=otitle.replace('\xa0\xa0','')
#                 data.append(otitle)
#             else:
#                 data.append(name[0])
#                 data.append('')
#
#             rate=re.findall(findRate,item)[0]
#             data.append(rate)
#
#             people=re.findall(findPeople,item)[0]
#             data.append(people)
#
#             inq=re.findall(findInq,item)
#             if len(inq)>0:
#                 inq=inq[0].replace('。','')
#                 data.append(inq)
#             else:
#                 data.append('')
#
#             bd=re.findall(findBd,item)[0]
#             bd=re.sub('<br(\s+)?/>(\s+)?','',bd)
#             bd=re.sub('/','',bd)
#             data.append(bd.strip())
#
#
#         return data
    except uerror.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)



if __name__ == '__main__':
    main()
    print('执行完毕')
