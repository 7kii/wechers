# -*- coding: utf-8 -*-
import web
import hashlib
import os
import time
import lxml
from lxml import etree
import service
import menu
import face
import piccut
import film
import wzry

urls = (
    '/', 'main'
)
target = 0

class main:
	
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.templates_root)
		self.token = 'kissss' #请按照公众平台官网\基本配置中信息填写
		self.AESKey = 'IBh2noM7QdzVBlbI2wklvggEWXM9vYzXGDSIHMQErIr'

	def GET(self):
		try:
			data = web.input()
			if len(data) == 0:
				return "hello, this is handle view"
				
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr

			list = [self.token, timestamp, nonce]
			list.sort()
			hash = hashlib.sha1()
			hash.update("".join(list).encode('utf-8'))
			hashcode = hash.hexdigest()

			print("handle/GET func: hashcode: "+ hashcode +" signature: "+ signature)
			if hashcode == signature:
				#menu.createMenu()
				return echostr
			else:
				return ""
		except:
			return ""
		
	def POST(self):
		global target
		str_xml = web.data()
		xml = etree.fromstring(str_xml)
		
		msgType=xml.find("MsgType").text
		fromUser=xml.find("FromUserName").text
		toUser=xml.find("ToUserName").text
		
		if msgType == 'text':
			content = xml.find("Content").text
			'''
			#print(content)

			if content == '1':
				target = 1
				return self.render.reply_text(fromUser, toUser, int(time.time()), "请发送图片")
				
			elif content == '2':
				target = 2
				return self.render.reply_text(fromUser, toUser, int(time.time()), "请发送图片")
				'''
			if content.lower().startswith(film.keywords):
				reslist = film.searchFilm(content)
				return self.render.reply_text(fromUser, toUser, int(time.time()), reslist)
			elif content.lower().startswith(wzry.keywords):
				reslist = wzry.searchAnswer(content)
				return self.render.reply_text(fromUser, toUser, int(time.time()), reslist)
			else:
				infos = service.getallService()
				return self.render.reply_text(fromUser, toUser, int(time.time()), infos)
		elif msgType == 'image':
			picurl = xml.find('PicUrl').text
			print('图片地址-------'+picurl)
			if target == 0 or target == 1:
				try:
					datas = face.imgtest(picurl)
					resback = '-------识别结果-------'
					for info in datas: 
						resback = resback + '\n 性别:'+datas[info][0]+','+' 年龄:'+datas[info][1]
					target = 0
					return self.render.reply_text(fromUser, toUser, int(time.time()), resback)
				except:
					return self.render.reply_text(fromUser, toUser, int(time.time()), '识别失败，换张图片试试吧')
				else:
					return self.render.reply_text(fromUser, toUser, int(time.time()), content)
					'''
			elif target == 2:
				try:
					piccut.cutBegin(picurl)
					target = 0
					return self.render.reply_article(fromUser, toUser, int(time.time()), '图片九宫格','图片切割成9块', picurl, '')
				except:
					return self.render.reply_text(fromUser, toUser, int(time.time()), '失败')
				else:
					return self.render.reply_text(fromUser, toUser, int(time.time()), content)
					'''
			else:
				return self.render.reply_text(fromUser, toUser, int(time.time()), "1111111")
		elif msgType == 'voice':
			return ""
		else:
			return ""

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()