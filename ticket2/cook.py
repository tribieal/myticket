import cherrypy, commands,os,urllib2
response = urllib2.urlopen('https://dynamic.12306.cn/otsweb/trainQueryAppAction.do?method=init&where=ypcx')
#put response to original info
original_info = response.read()
response.close()
print original_info
