import re
import time
import locale
import requests
import urllib.request
from selenium import webdriver


PhantomJS_Path = "D:\\Python\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"
Shopee_event_url = "https://shopee.tw/events3/code/4071189447/?smtt=201.6747"

def getImage():
	try:
		driver = webdriver.PhantomJS(executable_path=PhantomJS_Path)
		driver.get(Shopee_event_url)
		element = driver.find_element_by_id("voucher")
		image_url = element.get_attribute('src')
		return image_url
	except:
		return 0

def sendAlarm(sckey,title,content):
    alarmUrl = 'https://sc.ftqq.com/'+sckey+'.send?text='+urllib.parse.quote(title)+'&desp='+urllib.parse.quote(content)
    req = urllib.request.urlopen(alarmUrl)

def main():
	sckey_list = ['SCUxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','SCUxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']
	status = getImage()
	locale.setlocale(locale.LC_CTYPE, 'chinese')
	while True:
		if getImage() == 0 or getImage() == status:
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "尚未更新")
		else:
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + "已更新")
			status = getImage()
			#发
			for each in sckey_list:
				title = time.strftime('%m月%d日')+"虾皮优惠更新"
				url = Shopee_event_url
				content = " [查看详情]("+url+")"
				sendAlarm(each,title,content)
		time.sleep(120)


if __name__ == '__main__':
	main()
