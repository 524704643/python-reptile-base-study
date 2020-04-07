from lxml import etree
import requests
#定义请求头
url = 'http://www.zongheng.com/' #请求503 拒绝请求，需要进行请求头伪装
#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

#发送请求
res = requests.get(url=url,headers=headers) #伪装请求头后能请求
#获取响应状态码
code = res.status_code
print(code)
if code == 200:
    with open('./xpath.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
# 提取数据,可根据需求自行定义路径表达式
html = etree.parse('./xpath.html',etree.HTMLParser())
data = html.xpath('//ul[@class="news-lists"][1]//a/text()')
print(data)
data = html.xpath('//ul[@id="monthTicketRankList"]//a/text()')
print(data)
#属性多值匹配
data = html.xpath('//div[contains(@class,"top-title")]//div[contains(@class,"title")]/text()')
print(data)