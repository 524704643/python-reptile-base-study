from lxml import etree
import requests
#登录请求地址
loginurl = 'https://www.lmonkey.com/login'
#账户中心地址
targetUrl = 'https://www.lmonkey.com/my/order'
#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
#定义请求对象
req = requests.session()
#get登录界面先获取token以便进行下一步操作
res = req.get(url=loginurl,headers=headers)
if res.status_code == 200:
    print("响应成功")
    html = etree.HTML(res.text)
    #获取token的值
    r = html.xpath('//input[@name="_token"]/@value')[0]
    print(r)

    data = {
        '_token':r,
        'username':input("手机号"),
        'password':input("密码")
    }
    #post请求设置cookie，有token ，及用户cookie
    res = req.post(url=loginurl,headers=headers,data=data)

    if res.status_code == 200:
        print("登录成功")
        print(res.text)
        print("=========")
        #get请求获取订单页面
        res = req.get(url=targetUrl,headers=headers)
       # print(res.text)
        html = etree.HTML(res.text)
        r = html.xpath('//h5[@class="mb-1"]/text()')
        print(r)


