import re
varStr = input("请输入字符串")
#定义邮箱验证表达式 524704643@qq.com

#实例1、只允许汉字、英文字母、数字、下划线、英文句号、以及中划线组成
#“^”匹配邮箱的开始部分，用“$”匹配邮箱结束部分以保证邮箱前后不能有其他字符,只能输入指定的字符
reg = '^[A-Z,a-z,0-9,_,-,\u4e00-\u9fa5]+@[A-Z,a-z,0-9,_,-]+.com$'
res = re.search(reg,varStr)
if res == None:
    print("邮箱格式不正确，请重新输入")
else:
    print(res)