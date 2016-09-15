import urllib
import urllib2
import re
page = 1 
url = "http://www.qiushibaike.com/hot/page/" + str(page)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile(r'<div class="content">\s*<span>(?P<content>.*?)</span>\s*</div>')
	items = re.findall(pattern, content)
#print content
	for item in items:
		print item
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
