import urllib.request
import urllib.error

def check(url):
    try:
        res = urllib.request.urlopen(url, timeout=5)
        data = res.read(500).decode('utf-8', errors='replace')
        print(url, '->', res.status)
        print(data[:200])
    except urllib.error.HTTPError as e:
        print(url, 'HTTPError', e.code)
        print(e.read(200).decode('utf-8', errors='replace'))
    except Exception as e:
        print(url, 'ERROR', type(e).__name__, e)

if __name__ == '__main__':
    check('http://127.0.0.1:8000/')
    check('http://localhost:5175/')
