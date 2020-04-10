import requests

# 翻译的封装
def fanyi(kw):
    #请求url
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #需要进行翻译的数据
    data={
    'i':kw,
    'doctype':'json'
    }
    # post请求
    res = requests.post(url,data)
    #判断是否请求成功
    if res.status_code == 200:
        print("翻译成功")
        #输出翻译结果
        print(res.json()['translateResult'][0][0]['tgt'])

vars = '''
**********************
**欢迎进入py翻译工具**
**输入需要翻译的内容**
**   按q键进行退出  **
**********************
'''
print(vars)

while True:
    #输入需要翻译的内容
    kw = input('请输入翻译内容：')
    #若输入的内容是字符‘q’退出
    if kw == 'q':
        break
    #调用翻译工具
    fanyi(kw)