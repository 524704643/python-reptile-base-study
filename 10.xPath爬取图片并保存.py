from lxml import etree
import requests
from bs4 import BeautifulSoup
from urllib import request
import datetime

class reptailImages:
    #请求地址
    url = 'http://www.shuhai.com/shuku/0_0_0_0_0_0_0_2.html'
    soup = BeautifulSoup(open('xpath3.html', encoding='utf-8'), 'lxml')
    #定义请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    #爬取的图片数据
    images = []
    # get请求
    def __init__(self):
        res = requests.get(url=self.url,headers=self.headers)
        if res.status_code == 200:
            print("响应成功")
            with open('./xpath3.html','w',encoding='utf-8') as fp:
                fp.write(res.text)

            if self.parseImages():
                 self.writeImages()

    def parseImages(self):
        r = self.soup.select('.book-cover-wrapper a img', class_="book-cover")
        utlList = []
        for i in r:
            url = i.get("data-original")
            if url:
                utlList.append(url)
        print(utlList)
        self.images = utlList
        return True

    def writeImages(self):
        for i in range(0,len(self.images)):
            filename = './images/'+ str(datetime.datetime.now().timestamp())+'.jpg'
            request.urlretrieve(self.images[i],filename)

        print(self.images)

reptailImages()