import requests
from lxml import etree
import json


class xpathReptail:
    # 请求url
    url = 'https://www.lmonkey.com/essence'
    #定义请求头
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    #数据
    data=''
    # 发起get请求
    def __init__(self):
        res = requests.get(url=self.url,headers=self.headers)
        if res.status_code==200:
            print("响应成功,正在写入")
            with open('./xpath2.html','w',encoding='utf-8') as fp:
                fp.write(res.text)
            if self.parseData():
                self.writeData()


    #解析数据
    def parseData(self):
        html = etree.parse('./xpath2.html', etree.HTMLParser())
        authors = html.xpath('//div[contains(@class,"list-group-item-action")]//strong/a/text()')
        titles = html.xpath('//div[contains(@class,"list-group-item-action")]//div[contains(@class,"topic_title")]/text()')
        titleUrls = html.xpath('//div[contains(@class,"list-group-item-action")]//div[contains(@class,"flex-fill")]/a[1]/@href')
        # 整理数据
        data = []
        for i in range(0, len(authors)):
            res = {'author': authors[i], 'title': titles[i], 'url': titleUrls[i]}
            data.append(res)
        self.data = data
        print("解析数据")
        return True

    # 写入数据
    def writeData(self):
        #写入数据
        print("写入数据")
        with open('./xpath2.json','w') as fp :
            json.dump(self.data,fp)

#实例化
xpathReptail()
