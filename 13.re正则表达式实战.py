import requests,json,re
from lxml import etree

class ReClass:
    #请求url
    url = 'http://www.ybdu.co/list/1-1.html'
    # 定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    bookList = []
    #初始化
    def __init__(self):
        #发送请求
        res = requests.get(url=self.url,headers=self.headers)
        if res.status_code == 200:
            print("请求成功")
            #查看返回文本使用的编码，然后encoding=''就可以解决乱码问题
            print(res.encoding)
            with open('./re.html','w',encoding='ISO-8859-1') as fp:
                fp.write(res.text)
            res.encoding = 'ISO-8859-1'
            if self.parseData():
                self.writeJson()
    #解析数据
    def parseData(self):
        # 读取小说文本内容
        html = open("./re.html", "r")  # 读取文件
        html = html.read()   # 把文件内容转化为字符串
        # 获取小说标题
        # 定义正则表达式
        reg = "' >(.*?)</a></h4>"
        bookNames = re.findall(reg,html)
        print(bookNames)

        # 获取小说作者
        reg = "'>(.*?)</a></div>"
        authors = re.findall(reg,html)
        print(authors)

        # 获取小说图片url
        reg = ' <img src="(http://www.ybdu.co/files/article/image/.*?)" '
        imageUrls = re.findall(reg, html)
        print(imageUrls)
        bookList = list(zip(bookNames,authors,imageUrls))
        print(bookList)
        self.bookList = bookList
        return True

    def writeJson(self):
        datas = []
        result = ''
        for i in self.bookList:
            result = {"bookName":i[0],"author":i[1],"imageUrl":i[2]}
            datas.append(result)
        # 写入数据
        with open('./re.json','w') as fp:
            json.dump(datas,fp)

ReClass()