import requests

#定义请求url
url = 'http://httpbin.org/get'
#定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
# 代理ip
proxies = {
    'http':'121.237.149.163:3000',
    'https':'121.237.149.163:3000'
}
try:
    #发送请求
    res = requests.get(url,headers,proxies = proxies,timeout=5)
    #检测请求状态
    if res.status_code == 200:
        #输出ip地址
        print(res.json()['origin'])
except:
    print("代理ip失败")