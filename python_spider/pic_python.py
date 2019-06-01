import requests
import os
url="url"
root="D://文件名//"
path=root+url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("OK")
	else:
	    print("文件已存在")
except:
	print("爬取失败")
