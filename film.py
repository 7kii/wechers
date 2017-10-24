# -*- coding: utf-8 -*-
from tools import tmysql

fenable = True
keywords = 'dy'
introduce = '电影搜素：发送【' + keywords + '关键字】，举例:' + keywords + '星球大战'
#introduce += '\nPS：暂未开放【dy演员名】搜索，如有需求可留言'

def show():
	return fenable
	
def getFunInfo():
	return introduce
	
def parsePara(content):
	return content[2:]
	
def searchFilm(content):
	res = ''
	paraValue = parsePara(content)
	if paraValue != '' and paraValue != ' ' and paraValue != '  ':
		try:
			sql = 'select distinct(name), score, actor, introduce, udownload, upassword, uonlineshort from filminfo where name like "%%%%%s%%%%" or actor like "%%%%%s%%%%" and status = 0'  % (paraValue,paraValue)
			db = tmysql.Mysql()
			resfilm = db.getAll(sql)
			more = False
			if len(resfilm) > 0:
				res += '【本次共查询到' + str(len(resfilm)) + '部电影如下】'
				
				if len(resfilm) > 3:
					res += '\n【消息大小有限，只支持返回前3部，请提供更详细关键字准确查询】'
				if len(resfilm) == 1:
					more = True
					
				i = 1
				for film in resfilm:
					res += '\n' + '=======资源' + str(i) + '=======\n【片名】\n' + film['name'] + '\n【评分】\n' + film['score']
					if more:
						res += '\n【主演】\n' + film['actor'] + '\n【剧情】\n' + film['introduce'] 
					if film['uonlineshort'] != '':
						res += '\n【在线观看】\n' + film['uonlineshort']
					if film['udownload'] != '':
						res += '\n【磁力链接】\n' + film['udownload'] 
					if film['upassword'] != '':
						res += '\n【提取密码】\n' + film['upassword'] 
					if i >= 3:
						break
					i += 1
				
				res += '\n=================\n【复制磁力链接，迅雷或其他下载器新建任务即可下载】'
				res += '\n【在线观看地址需复制用浏览器打开】'
			else:
				res = '抱歉，暂未查到相关信息，敬请留言，周末更新，求关注'
		except Exception as e:
			res = '抱歉，暂未查到相关信息，敬请留言，周末更新，求关注'
			return res
	else:
		res = '请输入 dy关键字 查询'
	return res
	

	