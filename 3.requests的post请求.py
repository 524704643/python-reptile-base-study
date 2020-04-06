import requests
#定义utl
url = 'https://fanyi.baidu.com/sug'
#定义请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
str = input('请输入字符：')
#post请求的数据
data = {
    'kw':str
}
#发送post请求
res = requests.post(url=url,data=data,headers=headers)
#获取请求状态码
code = res.status_code
print(code)
if code==200:
    print('请求成功')
    respData = res.json()
    print(respData)
    if respData['errno']==0:
        print('响应成功')
        k = respData['data'][0]['k']
        v = respData['data'][0]['v'].split(';')[-2]
        print(k,"==",v)