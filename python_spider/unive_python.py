import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
	try:
		r=requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[3].string])
def printUnivList(ulist,num):
	print("{:^10}\t{:^6}\t{:^10}".format("paiming","name","zongfen"))
	for i in range(num):
		u=ulist[i]
		print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
if __name__ == '__main__':
	uinfo=[]
	url='view-source:http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
	html=getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,20)