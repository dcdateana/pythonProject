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

# 豆瓣爬取
from bs4 import BeautifulSoup as bs
import re
import xlwt
import sqlite3
import urllib.error as uerror


def main():
    baseurl='https://movie.douban.com/top250?start='
    dataList=getDate(baseurl)
    savePath='./'
    saveDate(savePath,dataList)

findlink=re.compile(r'<a href="(.*?)">')
findImage=re.compile(r'<img alt=".*?" class="" src="(.*?)" width="100"/>')
findName=re.compile(r'<span class="title">(.*?)</span>')
findRate=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findPeople=re.compile(r'<span>(\d*人评价)</span>')
findInq=re.compile(r'<span class="inq">(.*?)</span>')
findBd=re.compile('<p class="">\n(.*?)</p>',re.S)

def getDate(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        data=askUrl(url)
        datalist+=data
    # print(len(datalist))
    return datalist

def askUrl(url):
    datalist=[]
    head={}
    head['User-Agent']= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    req=ur.Request(url, method='GET',headers=head)
    try:
        response=ur.urlopen(req)
        html=response.read().decode('utf-8')
        # print(html)

# 解析
        soup=bs(html,'html.parser')
        for item in soup.find_all('div',class_ = "item"):
            # print(item)
            data=[]
            item=str(item)

            link=re.findall(findlink,item)[0]
            data.append(link)

            imgSrc=re.findall(findImage,item)[0]
            data.append(imgSrc)

            name=re.findall(findName,item)
            if len(name)==2:
                data.append(name[0])
                otitle=name[1].replace('/','')
                otitle=otitle.replace('\xa0\xa0','')
                data.append(otitle)
            else:
                data.append(name[0])
                data.append('')

            rate=re.findall(findRate,item)[0]
            data.append(rate)

            people=re.findall(findPeople,item)[0]
            data.append(people)

            inq=re.findall(findInq,item)
            if len(inq)>0:
                inq=inq[0].replace('。','')
                data.append(inq)
            else:
                data.append('')

            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?','',bd)
            bd=re.sub('/','',bd)
            data.append(bd.strip())

            datalist.append(data)
        return datalist
    except uerror.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

def saveDate(savePath,datelist):

    # 保存到excel
    workBook=xlwt.Workbook(encoding='utf-8')
    worksheet=workBook.add_sheet('sheet1')

    for x in range(0,250):
        for y in range(0,8):
            worksheet.write(x,y,datelist[x][y])
    workBook.save(savePath+'movie.xls')

    # 保存到数据库
    connect=sqlite3.connect('movie.db')
    cursor=connect.cursor()
    sql='''
        create table movie250
        (id integer primary key autoincrement ,
        info_link text,
        pic_linc text,
        cname varchar,
        ename varchar,
        score varchar,
        rated varchar,
        instroduction text,
        info text
        );
    '''
    cursor.execute(sql)
    for x in range(0,250):
        sql=f'''
            insert into movie250 values ({x+1},{'"'+datelist[x][0]+'"'},{'"'+datelist[x][1]+'"'},{'"'+datelist[x][2]+'"'},{'"'+datelist[x][3]+'"'},
            {'"'+datelist[x][4]+'"'},{'"'+datelist[x][5]+'"'},{'"'+datelist[x][6]+'"'},{'"'+datelist[x][7]+'"'});
        '''
        cursor.execute(sql)

    connect.commit()
    connect.close()

if __name__ == '__main__':
    main()
    print('执行完毕')
