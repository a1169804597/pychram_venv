import http.cookiejar,urllib.request
#用urllib库将一个网址的cookies保存到一个文件中
filename='cookies.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response= opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)


# 导入cookies并且使用
# cookie=http.cookiejar.MozillaCookieJar()
# cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response= opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))