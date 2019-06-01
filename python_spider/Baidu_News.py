#coding=utf-8
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    '''
    :param url:
    :return:html
    '''
    try:
        kv = {'user-agent': 'Mozilla/5.0'} #防止反爬
        r = requests.get(url,timeout=30 ,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding #防止编码问题
        return r.text
    except:
        return "爬取失败"
def parsePage(ilt, html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        message=soup.find_all(name='p', attrs={"class": "c-author"})
        for me in range(len(message)):
            ilt.append(message[me].string)
    except:
        print("parsePage error")
def printGoodsList(ilt):
    fileObject = open('result.txt', 'w+')
    fileObject.write(__builtins__.str(ilt))
    fileObject.write('\n')
    fileObject.close()
if __name__ == '__main__':
    depth = 70#爬取70页
    start_url = 'http://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E6%91%A9%E6%8B%9C&x_bfe_rqs=03E80&x_bfe_tjscore=0.003390&tngroupname=organic_news&rsv_dl=news_b_pn&pn='
    infoList = []
    for i in range(depth):
        try:
            url = start_url + str(10*i)
            print('正在爬取第',i+1,'页')
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    print('爬取完成')
