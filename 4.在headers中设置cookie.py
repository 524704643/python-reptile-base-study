import requests
#定义请求头
url = 'https://www.lmonkey.com/users/pErGGZ8yd/edit'
#定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #在headers中携带cookie信息
    'Cookie':'__guid=168986279.4117794973237464600.1586235742524.4229; UM_distinctid=17153049dbf2dc-09dce81f762cab-5d4e211f-ff000-17153049dc01c6; href=https%3A%2F%2Fwww.lmonkey.com%2Fregister; wechat_flag=eyJpdiI6Ijd3NGQyRlE4eVM1K1gxSTZFRDI0TGc9PSIsInZhbHVlIjoiMUhQNlNjZ25UWDMwMW9LM0VBWGlNOTdiSDFcL2hWaUVXRTRYQ2ZQUDFxN1kzaDhaNURJOElTMkxpXC9RY29JelJNIiwibWFjIjoiZTA0ZmE1OTRlODQxZTc2NTcwMWFkODJkZmEzYjgzOTM3ZmFmN2UzNGE1ZjA3Yjg2ZjgwNzA1NzJiOTkwNzg4MCJ9; XSRF-TOKEN=eyJpdiI6ImxNbGNEdmtaUVN3bzU4eXR1NVR3REE9PSIsInZhbHVlIjoiOUc1dXM5SjBNc3Q4ZGgwYkRJUzVoR1pINXhyS1JqVVRFQm1NSmNLWWc1QXFXTXNqS08zQkFRbVZURlRQQjJcL3MiLCJtYWMiOiJkOGYyM2Y2NmNhZDg1M2M4Yzk4MTQ0OGQ4ZGIxNGYxMWE3NTRmODFjODMwMDljYzk5MmM2MTUwNmQwYmE0MDdkIn0%3D; _session=eyJpdiI6IlwvMHErZWVqUlhJXC9YQ0IzeW9DV2ludz09IiwidmFsdWUiOiJhXC80dFFRcHpWVGZiWGh2REtWXC9cLzErRFppV2lRV3lETUp5QWtRXC9GWnI2YWpYYzlkeEVlY1ZQZU1ENTM4eVZJeSIsIm1hYyI6IjI1OWY0ZjgxNjM0YjlhNjU5YTM0NThhNWI5NjEzNThhMjIxZDZjMmIxMGJhNjMwZDNmNTYxZTQ5MjVjODAwYmEifQ%3D%3D; monitor_count=21; Hm_lvt_676e52e2eddd764819cab505b21e9ee8=1586235744; Hm_lpvt_676e52e2eddd764819cab505b21e9ee8=1586236147; CNZZDATA1277679765=524955651-1586235744-https%253A%252F%252Fwww.baidu.com%252F%7C1586235744; qimo_seosource_ad8e1ca0-2091-11ea-af9d-6523a0f144a7=%E7%AB%99%E5%86%85; qimo_seokeywords_ad8e1ca0-2091-11ea-af9d-6523a0f144a7=; accessId=ad8e1ca0-2091-11ea-af9d-6523a0f144a7'
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
