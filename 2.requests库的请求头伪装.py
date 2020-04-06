import requests
#定义请求头
#url = 'https://hoho.website/' #请求成功
url = 'https://www.xicidaili.com/' #请求503 拒绝请求，需要进行请求头伪装
#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

#发送请求
res = requests.get(url=url,headers=headers) #伪装请求头后能请求
#获取响应状态码
code = res.status_code
print(code)
#将响应的内容写入文件
if code==200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
