# -*- coding: utf-8 -*-
import hashlib
import web
import time
import os

urls = (
    '/', 'index'
)

class index:
	
	def GET(self):
	
		print(11111)
		'''
		#获取输入参数
		data = web.input()
		signature=data.signature
		timestamp=data.timestamp
		nonce=data.nonce
		echostr=data.echostr
		
		print(data)
		
		#自己的token
		token="kisss" #这里改写你在微信公众平台里输入的token
		#字典序排序
		list=[token,timestamp,nonce]
		list.sort()
		sha1=hashlib.sha1()
		map(sha1.update,list)
		hashcode=sha1.hexdigest()
		#sha1加密算法        
		print("======="+hashcode)
		#如果是来自微信的请求，则回复echostr
		#if hashcode == signature:
		return echostr
		'''
		url = 'C:/myweb/kisss/piccut/2017081001455166/2017081001455166_0.png'
		return url
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()