from bs4 import BeautifulSoup
import datetime
from urllib import request

#创建一个BeautifulSoup4对象
soup = BeautifulSoup(open('xpath3.html',encoding="utf-8"),'lxml')
#1、通过标签获取文档数据（单值获取【默认获取第一个符合要求的】）

# 获取title标签
r = soup.title
# 获取div标签下的span标签下的a标签
r = soup.div.span.a
# 获取div标签且具有class声明的标签
r = soup.div['class']
#获取指定标签下的文本内容
r = soup.div.span.a.string

#2、通过搜索获取多值文档数据（可多值搜索）

#获取满足div的第一个标签内容
r = soup.find('div')
# 获取所有的a标签
r = soup.find_all('a')


# 3、根据css选择获取内容
# 获取类名选择器
r = soup.select('.book-cover-wrapper')
# 获取id选择器
r = soup.select('#hottagid')
#获取空格 层级关系选择器
r = soup.select("div div div a img")
#获取逗号选择器，并列选择器
r = soup.select("img,span")

r = soup.select('.book-cover-wrapper a img',class_="book-cover")
print(r)
#遍历
utlList = []
for i in r:
    url = i.get("data-original")
    if url:
        utlList.append(url)

# 爬取图片
for i in range(0,len(utlList)):
     filename = './images/'+ str(datetime.datetime.now().timestamp())+'.jpg'
     request.urlretrieve(utlList[i],filename)

print(utlList)