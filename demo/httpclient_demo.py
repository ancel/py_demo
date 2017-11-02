import requests
SESSION = requests.Session()

url = 'http://www.baidu.com'
r = SESSION.get(url,timeout=30)
print(r.status_code)
print(r.text)