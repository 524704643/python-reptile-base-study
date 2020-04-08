#导入requests
import requests

#定义url
url = 'https://www.baidu.com';
#发送请求
res = requests.get(url=url)
#响应请求
print(res)
print("---------")
print(res.content) #b'...' 二进制的文本流
print("---------")
print(res.content.decode("utf-8"))
print("---------")
print(res.headers) #获取响应头信息
print("---------")
print(res.request.headers) #获取请求的头信息
print("---------")
print(res.text)  #获取响应的内容
print("---------")
print(res.status_code) #获取请求状态码
print("---------")
print(res.url) #请求的url地址
