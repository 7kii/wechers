# -*- coding: utf-8 -*-
from tools import tmysql

fenable = True
keywords = 'wz'
introduce = '王者荣耀-夫子的试炼 查询：发送【' + keywords + '关键字】，举例:' + keywords + '暴君'
#introduce += '\nPS：暂未开放【dy演员名】搜索，如有需求可留言'

def show():
	return fenable
	
def getFunInfo():
	return introduce
	
def parsePara(content):
	return content[2:]
	
def searchAnswer(content):
	res = ''
	paraValue = parsePara(content)
	if paraValue != '' and paraValue != ' ' and paraValue != '  ':
		try:
			sql = 'select question, answer from wzry where question like "%%%%%s%%%%" ORDER BY aid desc'  % (paraValue)
			db = tmysql.Mysql()
			resfilm = db.getAll(sql)
			more = False
			if len(resfilm) > 0:
				res += '【本次查询结果如下】'
					
				i = 1
				for film in resfilm:
					res += '\n' + '-------------------'
					if film['question'] != '':
						res += '\n【问题】\n' + film['question']
					if film['answer'] != '':
						res += '\n【答案】\n' + film['answer'] 

					i += 1
			else:
				res = '抱歉，暂未查到相关信息'
		except Exception as e:
			res = '抱歉，暂未查到相关信息'
			return res
	else:
		res = '请输入 wz关键字 查询'
	return res
	

	