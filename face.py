# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import re

fenable = True
introduce = '年龄检测：请发送图片'

def show():
	return fenable

def imgtest(picurl):

	url = 'https://how-old.net/Home/Analyze?isTest=False&source=&version=how-old.net'
	headers = {
		'Accept-Encoding':'gzip, deflate, br',
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
		'Host': "how-old.net",
		'Referer': "http://how-old.net/",
		'X-Requested-With': "XMLHttpRequest"
	}

	values = {
		"faceUrl": picurl
	}
	
	print(picurl)
	
	data = urllib.parse.urlencode(values).encode('utf-8')
	req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
	response = urllib.request.urlopen(req)
	resinfo = response.read().decode('utf8')
	
	info = resinfo.replace('\\','')
	gender = re.findall(r'"gender": "(.*?)"rn', info)
	age = re.findall(r'"age": (.*?),rn', info)

	resback = {}
	for index in range(len(gender)):
		if gender[index] == 'Male':
			gender1 = '男'
		else:
			gender1 = '女'
		resback[index] = gender1,age[index]
	return resback
	
def getFunInfo():
	return introduce
	