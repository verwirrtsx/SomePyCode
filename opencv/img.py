import requests
import time
import redis
#import flask,json
import qrcode
import pyzbar.pyzbar as pyzbar
from PIL import ImageFilter 
from PIL import Image,ImageEnhance

def getCode(url):
	pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
	r = redis.Redis(connection_pool=pool)
	r.rpush("img", 11, 22, 33)
	try:
		img_code = r.get('img')
	except :
		print('img_code')

	img = requests.get(url)
	with open('1.jpg','wb') as f:
		f.write(img.content)

	I = Image.open('C:\\Users\\Administrator\\Desktop\\some\\py\\opencv\\1.jpg')

	try:
		en=ImageEnhance.Contrast(I) #增加对比度
		en_end=en.enhance(10)
		en_end.save('2.jpg')
		#url = pyzbar.decode(Image.open('C:\\Users\\Administrator\\Desktop\\some\\py\\opencv\\2.jpg'), symbols=[pyzbar.ZBarSymbol.QRCODE])[0][0].decode('utf-8')

	except:
		print('shen ma gui tu')
		exit()

	code_url = pyzbar.decode(Image.open('C:\\Users\\Administrator\\Desktop\\some\\py\\opencv\\2.jpg'), symbols=[pyzbar.ZBarSymbol.QRCODE])[0][0].decode('utf-8')
	shop = 'payapp.weixin.qq.com'

	user = 'wxp://'

	if shop in code_url or user in code_url:
		print('weixin 111')
	else:
		print('disanfan 2222')
		print(code_url)

	img = qrcode.make(code_url)
	with open('test.png', 'wb') as f:
	    img.save(f)

getCode('http://ptc.aibtc.top/Uploads/payqrcode/5dcb64a096c4c.jpg')

#r,g,b = I.split()  ##通道分离
#g.show()
#bluF = I.filter(ImageFilter.BLUR)           ##均值滤波      
#conF = I.filter(ImageFilter.CONTOUR)  ##找轮廓
#edgeF = I.filter(ImageFilter.FIND_EDGES)         ##边缘检测
#I.show()
#edgeF.show()
#conF.save('2.jpg')
#conF.show()
#L = I.convert('L')
#L.save('2.jpg')
#L.show()