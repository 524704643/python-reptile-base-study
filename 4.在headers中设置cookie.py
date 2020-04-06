import requests
#定义请求头
url = 'http://www.rrys2019.com/user/user'
#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #在headers中携带cookie信息
    'Cookie':'__guid=65356968.1592317744388106000.1586187141791.5054; UM_distinctid=171501f0aec65-0df7ed5d040458-5d4e211f-ff000-171501f0aed269; __gads=ID=b04147056b7a5b53:T=1586187144:S=ALNI_MbCkB4QL8qdz86iQRWdTxh3oswceA; jmtm978=1; PHPSESSID=8dn2br9rhq21n24uno512d4ii3; GINFO=uid%3D9300093%26nickname%3Dkongxin2020%26group_id%3D0%26avatar_t%3D%26main_group_id%3D%26common_group_id%3D; GKEY=582212b405146816151990fda9cc3088; monitor_count=9; cps3=vmall%2F1586187143%3Bxmyp%2F1586187265%3Bvip%2F1586187274; CNZZDATA1254180690=1284506452-1586183980-null%7C1586183980; CNZZDATA1275589337=1814261288-1586183725-null%7C1586183725'
}
#发送请求
res = requests.get(url=url,headers=headers)#伪装请求头后能请求
#获取响应状态码
code = res.status_code
print(code)
#将响应的内容写入文件
if code==200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
