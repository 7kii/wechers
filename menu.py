# -*- coding: utf-8 -*-
import other
import face
import piccut
import film

fucList = [face, piccut, film, other]

def getall():
	fucMenu = '-----功能列表-----'
	i = 1;
	for fuc in fucList:
		if fuc.show():
			fucMenu += '\n' + str(i) + ' : ' + fuc.getFunInfo()
			i = i + 1
	return fucMenu
