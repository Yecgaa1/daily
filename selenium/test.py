import urllib3
import cookielib
from bs4 import BeautifulSoup
#设置代理IP
proxy_support = urllib3.ProxyHandler({'http':'120.197.234.164:80'})
#设置cookie
cookie_support = urllib3.HTTPCookieProcessor(cookielib.LWPCookieJar())
opener = urllib3.build_opener(proxy_support,cookie_support,urllib.HTTPHandler)
urllib3.install_opener(opener)
#开始的URL
#hosturl = "http://www.renren.com"
hosturl = "http://mail.163.com/"
#接受表单数据的URL
#posturl = "http://www.renren.com/ajaxLogin/login"
posturl = "https://mail.163.com/entry/cgi/ntesdoor?df=mail163_letter&from=web&funcid=loginone&iframe=1&language=-1&passtype=1&product=mail163&net=e&style=-1&race=118_35_39_bj&uid=Thinkgamer@163.com"
#发送表单数据
postdata = urllib.urlencode(
  {
  "username":"xxxxxxxxxxx",
  "password":"xxxxxxxxxxxxxxx"
  }
)
#设置表头
headers = {
  #'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0/',
  #'Referer':'http://www.renren.com/'
  'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
  'Referer':'http://mail.163.com/'
}
#生成HTTP请求
req =urllib.Request(
  url = posturl,
  data = postdata,
  headers = headers
)
print(req)
page = urllib.urlopen(req).read()
print(page)
listvalue = page.split(";")
url = listvalue[0].split("op.location.href = ")[1]
href = url[1:-1]
print(href)
soup = BeautifulSoup(urllib.urlopen(href))
print(soup.title)