# coding=gbk
import string
from urllib import request  
from bs4 import BeautifulSoup            #Beautiful Soup��һ�����Դ�HTML��XML�ļ�����ȡ�ṹ�����ݵ�Python��
from urllib.parse import urlparse
import re

#����ͷ�ļ���ģ�����������

url_source="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017"
url=url_source+"/index.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
charset='gbk'

result1=[]
####################################################################################################
def html_list1(url,headers,charset):
	page = request.Request(url,headers=headers)  
	page_info = request.urlopen(page).read().decode(charset)#��Url,��ȡHttpResponse���ض��󲢶�ȡ��ResposneBody

	# ����ȡ��������ת����BeautifulSoup��ʽ������html.parser��Ϊ������  
	soup = BeautifulSoup(page_info, 'html.parser')  
	# �Ը�ʽ������ʽ��ӡhtml
	List_html = soup.find_all("a",href=re.compile('.html'))  # ��������href�а���html�����

	# ��ӡ���ҵ���ÿһ��a��ǩ��string���������� 
	for html in List_html:
		#��ȡ�����������������
		bs = BeautifulSoup(str(html).replace('<br/>',''),'html.parser')

		tmp=[]

		tmp.append(bs.a["href"].replace(".html",""))#���������������
		tmp.append(bs.string)#���������������
		tmp.append(url_source+"/"+bs.a["href"])  # ���url
		result1.append(tmp)
####################################################################################################
html_list1(url,headers,charset)
####################################################################################################
result2=[]
def html_list2(url, headers, charset):
	page = request.Request(url, headers=headers)
	page_info = request.urlopen(page).read().decode(charset)  # ��Url,��ȡHttpResponse���ض��󲢶�ȡ��ResposneBody

	# ����ȡ��������ת����BeautifulSoup��ʽ������html.parser��Ϊ������
	soup = BeautifulSoup(page_info, 'html.parser')
	# �Ը�ʽ������ʽ��ӡhtml
	List_html = BeautifulSoup(page_info, 'html.parser').find_all('tr', class_="citytr")  # ��������href�а���html�����
	# ��ӡ���ҵ���ÿһ��a��ǩ��string����������
	for html in List_html:
		# ��ȡ�����������������
		bs = BeautifulSoup(str(html).replace('<br/>', ''), 'html.parser')
		res=bs.find_all("a",href=re.compile(".html"))
		tmp = []

		tmp.append(res[0].string)  # ���������������
		tmp.append(res[1].string)  # ���������������
		tmp.append( url_source + "/" + BeautifulSoup(str(res[0]), 'html.parser').a["href"])  # ���url
		result2.append(tmp)
####################################################################################################

####################################################################################################
result3=[]
def html_list3(url, headers, charset):
	try:
		page = request.Request(url, headers=headers)

		page_info = request.urlopen(page).read().decode(charset)  # ��Url,��ȡHttpResponse���ض��󲢶�ȡ��ResposneBody
		if any(page_info):
			# ����ȡ��������ת����BeautifulSoup��ʽ������html.parser��Ϊ������
			# �Ը�ʽ������ʽ��ӡhtml
			List_html = BeautifulSoup(page_info, 'html.parser').find_all('tr',class_="countytr")  # ��������href�а���html�����
			#if ( any(List_html) == False ):
			#	print(url);
			#	List_html = BeautifulSoup(page_info, 'html.parser').find_all('tr', class_="towntr")
			# ��ӡ���ҵ���ÿһ��a��ǩ��string����������
			for html in List_html:
				# ��ȡ�����������������
				bs = BeautifulSoup(str(html).replace('<br/>', ''), 'html.parser')

				res = bs.find_all("td")
				tmp = []

				tmp.append(res[0].string)  # ���������������
				tmp.append(res[1].string)  # ���������������

				if any(BeautifulSoup(str(res[0]), 'html.parser').find_all("a")):
					tmp.append(url[0:-10] + "/" + BeautifulSoup(str(res[0]), 'html.parser').a["href"])  # ���url
				else:
					tmp.append(None)

				result3.append(tmp)
		else:
			print("�޷���ȡҳ�棺"+url)


	except BaseException:
		print(str(BaseException) + "   " + url)
####################################################################################################

for url in result1:
	html_list2(url[2],headers,charset)



for url in result2:
		html_list3(url[2],headers,charset)

result=result1+result2+result3


# #open()�Ƕ�д�ļ��ĺ���,with�����Զ�close()�Ѵ��ļ�
#print(result1)
#print(result2)
#print(result3)
#print(result)
with open(r"D:\a.csv","w") as file:       #�ڴ�����ֻд�ķ�ʽ��/����һ����Ϊ articles ��txt�ļ�
	for city in result:
		file.write(city[0]+','+city[1]+'\n')

