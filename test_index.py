import requests


headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip,deflate, lzma, sdch",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "Content-Type": "application/json",
           "Connection": "keep-alive",
           "Host": "maprun.hustonline.net",
           "pgrade-Insecure-Requests": 1,
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71"
                         " Safari/537.36 OPR/33.0.1990.43"
}

data = '{"token": "3333331135455"}'
url = 'http://127.0.0.1:5000/api/post'
r = requests.post(url, data=data)

print r.text