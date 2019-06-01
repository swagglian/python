import requests
url = "http://www.ip138.com/ips138.asp?ip="
try:
	r=requests.get(url+'IPaddress')
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.text[-500:])
except:
	print("error")
