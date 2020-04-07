from lxml import etree

text='''
<html>
<body>
<ul>
		<a target="_blank" href="//www.17k.com/"><span>首页</span></a>
		<a target="_blank" href="//www.17k.com/top/"><span>排行榜</span></a>
		<a target="_blank" href="//www.17k.com/all"><span>分类</span></a>
		<a target="_blank" href="//author.17k.com"><span>我要写书</span></a>
		<a target="_blank" href="//www.17k.com/man/"><span>17K男生</span></a>
		<a target="_blank" href="//www.17k.com/mm/"><span>四月天女生</span></a>
		<!--<a target="_blank" href="//www.17k.com/gexing/"><span>个性小说</span></a>-->
		<!--<a target="_blank" href="//www.17k.com/chuban/"><span>出版</span></a>-->
		<a target="_blank" href="//www.17k.com/ip/"><span>IP改编</span></a>
		<a target="_blank" href="//www.17k.com/mianfei/"><span>免费小说</span></a>
		<a target="_blank" href="//www.17k.com/quanben/"><span>完本小说</span></a>
		<a class="mobile" href="//www.17k.com/download/"><span>手机端</span>
</ul>
</body>
</html>
'''
# 提取数据
html = etree.HTML(text)
data = html.xpath('/html/body/ul/a/span/text()')
print(data)