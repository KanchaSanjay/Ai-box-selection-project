import json
import urllib.request
import urllib.error

url = 'http://127.0.0.1:8000/api/recommend-box/'
body = {'products': [1]}
req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), headers={'Content-Type': 'application/json'})
try:
    res = urllib.request.urlopen(req)
    print('STATUS', res.status)
    print(res.read().decode())
except urllib.error.HTTPError as e:
    print('HTTPError', e.code)
    print(e.read().decode())
except Exception as e:
    print(type(e).__name__, e)
