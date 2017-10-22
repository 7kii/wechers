# -*- coding: utf-8 -*-
import os
import time
import random
import urllib.request
from PIL import Image

fenable = False
introduce = '图片切割：请发送2后发送图片'

def show():
	return fenable
	
def getFunInfo():
	return introduce
    
def splitimage(src, rownum, colnum, dstpath):
	img = Image.open(src)
	w, h = img.size
	if rownum <= h and colnum <= w:
		print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
		print('开始处理图片切割, 请稍候...')

		s = os.path.split(src)
		if dstpath == '':
			dstpath = s[0]
		fn = s[1].split('.')
		basename = fn[0]
		ext = fn[-1]

		num = 0
		rowheight = h // rownum
		colwidth = w // colnum
		for r in range(rownum):
			for c in range(colnum):
				box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
				img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
				num = num + 1

		print('图片切割完毕，共生成 %s 张小图片。' % num)
	else:
		print('不合法的行列切割参数！')

def cutBegin(url):
	#path = input('请输入图片文件路径：')
	seri = getSerialNum()
	name = seri + '.png'
	dstpath = 'C:/myweb/kisss/piccut/' + seri + '/'
	
	print(dstpath)
	os.mkdir(dstpath)

	file = dstpath + name
	urllib.request.urlretrieve(url, file) 

	if os.path.isfile(file):
		#dstpath = input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
		dstpath = ''
		if (dstpath == '') or os.path.exists(dstpath):
			row = 3 #int(input('请输入切割行数：'))
			col = 3 #int(input('请输入切割列数：'))
			if row > 0 and col > 0:
				splitimage(file, row, col, dstpath)
			else:
				print('无效的行列切割参数！')
		else:
			print('图片输出目录 %s 不存在！' % dstpath)
	else:
		print('图片文件 %s 不存在！' % src)

		
def getSerialNum():
	seri = random.randint(10, 99)
	sss = time.strftime("%Y%m%d%H%M%S") ##24小时格式
	num = str(sss) + str(seri)
	#print(num)
	return num
