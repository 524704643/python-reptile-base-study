import requests

#需要请求的目标地址
url = 'http://www.rrys2019.com/user/user'
#登录请求的地址
loginUrl = 'http://www.rrys2019.com/User/Login/ajaxLogin'

#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
#如果需要爬虫程序主动记录cookie并且携带cookie，那么在使用requests之前先调用session方法
#使用session方法返回的对象发送请求即可
req = requests.session()
#登录请求时的数据
data = {
    'account':'524704643@qq.com',
    'password':'Qq3983488123',
    'remember':'1',
    'url_back':'http://www.rrys2019.com/user/user',
}
#发起登录请求
res = req.post(url=loginUrl,headers=headers,data=data)
#判断状态
code = res.status_code
print(code)
if code == 200:
    print('响应成功')
    res = req.get(url=url,headers=headers)
    with open('./session-success.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
