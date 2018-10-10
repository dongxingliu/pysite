# coding=gbk
import string
from urllib import request  
from bs4 import BeautifulSoup            #Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库
from urllib.parse import urlparse
import re

#构造头文件，模拟浏览器访问

url_source="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017"
url=url_source+"/index.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
charset='gbk'

result1=[]
####################################################################################################
def html_list1(url,headers,charset):
	page = request.Request(url,headers=headers)  
	page_info = request.urlopen(page).read().decode(charset)#打开Url,获取HttpResponse返回对象并读取其ResposneBody

	# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器  
	soup = BeautifulSoup(page_info, 'html.parser')  
	# 以格式化的形式打印html
	List_html = soup.find_all("a",href=re.compile('.html'))  # 查找所有href中包含html的语句

	# 打印查找到的每一个a标签的string和文章链接 
	for html in List_html:
		#获取行政区划代码和名称
		bs = BeautifulSoup(str(html).replace('<br/>',''),'html.parser')

		tmp=[]

		tmp.append(bs.a["href"].replace(".html",""))#添加行政区划代码
		tmp.append(bs.string)#添加行政区划名称
		tmp.append(url_source+"/"+bs.a["href"])  # 添加url
		result1.append(tmp)
####################################################################################################
html_list1(url,headers,charset)
####################################################################################################
result2=[]
def html_list2(url, headers, charset):
	page = request.Request(url, headers=headers)
	page_info = request.urlopen(page).read().decode(charset)  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody

	# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
	soup = BeautifulSoup(page_info, 'html.parser')
	# 以格式化的形式打印html
	List_html = BeautifulSoup(page_info, 'html.parser').find_all('tr', class_="citytr")  # 查找所有href中包含html的语句
	# 打印查找到的每一个a标签的string和文章链接
	for html in List_html:
		# 获取行政区划代码和名称
		bs = BeautifulSoup(str(html).replace('<br/>', ''), 'html.parser')
		res=bs.find_all("a",href=re.compile(".html"))
		tmp = []

		tmp.append(res[0].string)  # 添加行政区划代码
		tmp.append(res[1].string)  # 添加行政区划名称
		tmp.append( url_source + "/" + BeautifulSoup(str(res[0]), 'html.parser').a["href"])  # 添加url
		result2.append(tmp)
####################################################################################################

####################################################################################################
result3=[]
def html_list3(url, headers, charset):
	try:
		page = request.Request(url, headers=headers)

		page_info = request.urlopen(page).read().decode(charset)  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
		if any(page_info):
			# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
			# 以格式化的形式打印html
			List_html = BeautifulSoup(page_info, 'html.parser').find_all('tr',class_="countytr")  # 查找所有href中包含html的语句
			#if ( any(List_html) == False ):
			#	print(url);
			#	List_html = BeautifulSoup(page_info, 'html.parser').find_all('tr', class_="towntr")
			# 打印查找到的每一个a标签的string和文章链接
			for html in List_html:
				# 获取行政区划代码和名称
				bs = BeautifulSoup(str(html).replace('<br/>', ''), 'html.parser')

				res = bs.find_all("td")
				tmp = []

				tmp.append(res[0].string)  # 添加行政区划代码
				tmp.append(res[1].string)  # 添加行政区划名称

				if any(BeautifulSoup(str(res[0]), 'html.parser').find_all("a")):
					tmp.append(url[0:-10] + "/" + BeautifulSoup(str(res[0]), 'html.parser').a["href"])  # 添加url
				else:
					tmp.append(None)

				result3.append(tmp)
		else:
			print("无法获取页面："+url)


	except BaseException:
		print(str(BaseException) + "   " + url)
####################################################################################################

for url in result1:
	html_list2(url[2],headers,charset)



for url in result2:
		html_list3(url[2],headers,charset)

result=result1+result2+result3


# #open()是读写文件的函数,with语句会自动close()已打开文件
#print(result1)
#print(result2)
#print(result3)
#print(result)
with open(r"D:\a.csv","w") as file:       #在磁盘以只写的方式打开/创建一个名为 articles 的txt文件
	for city in result:
		file.write(city[0]+','+city[1]+'\n')

