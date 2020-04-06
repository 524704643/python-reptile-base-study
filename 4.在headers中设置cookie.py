import requests
#定义请求头
url = 'https://hoho.website/admin/main'
#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #在headers中携带cookie信息
    'Cookie':'__guid=151756704.254505745216676030.1583504075433.185; JSESSIONID=E263FC9050EF4C06EC15471C898CA752; rememberMe=x+g5mLoVIljje+6zbnZNUKbXqC1kfXvgL3I/1plo1HMah6Kunwgse9cLLBaMzqj0W2uVqGY+aGiOu89vnf2nJUBPSdjBxeP6D69+3HSDM7r8El0ga4p0BhOJ6HyNk8DP7AFb8RaOhm04LRCcOAXLe+ilsTyRR6kdcz6kpjN+vZbCvEdLdtKQokxHJ3wPZalt+bLrSB1NrCdkAnFzRgosHSFliLfL3SQ7v7wY9GRP/RuwoV0X6Th/2/EfXV0P8hb3uD3UypY4bOtDvfDAGXEDic6Do3iS3EErj6zeqCewHgXjWb+J8Xglu5FSQb4wt4SWdnX75KXplKG/NqxLhllSJiym0H15LTMTQR7jj3MMSLPUruGnkIBLUw4c6x9daW4I5+XcjRh1Puo8ugYoD9ZfAgeBfBXbgB7vSyUamdnAZP5WrM0NPUSlD22sO+mcMLZesoWx7xWGgZyIF6pX6hOTyZ2AVx8OVPf3HPXeVzs4AI9RBKfDdNL5fw84xB4P5dCQCqJemRW2ix6ekg3lEc1JEM0t/SBHnUd8RqDBcHE7ENDhw5hy4Mltkc9fQPF2YhVkqyx3sD1TGsUolezHTb0Uha5cGX2EeAi35QoD1rtj9pt62Yo7VMU/Re5c5/foLjpaXrKP59Vi2DRgoq3gIboZSVFeDal8NivNZjinGpI=; monitor_count=15'
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
