import requests
import re
from bs4 import BeautifulSoup
import sys

countID = 1
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
cookiesStr = '_ga=GA1.2.1316280964.1516605373; _gid=GA1.2.275832695.1516605373; __utmc=129582553; __utmz=129582553.1516669378.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=129582553.1903475512.1516605038.1516684113.1516689876.5; __utmt=1; DRUGSSESSIONID=A391DDBBC3C893AA6FF5A2DF68AE193C-n1; _gat=1; JUTE_BBS_DATA=d0dfd6fd94333d210821b7e9370decbbac4698f9266108a11f26511cd76f520183d2efb641b8a55171b2e35a36968d7d2b0b459e2bfa051d5bd3c0c061b12ca6e3a3d619877b4404787147ac48231d34; __utmb=129582553.14.10.1516689876'
def getCookies(cookiesStr):
	cookies = {}
	for line in cookiesStr.split(';'):
		key, value = line.split('=', 1)
		key = key.strip()
		value = value.strip()
		cookies[key] = value
	return cookies

cookies = getCookies(cookiesStr)


def getHtmlString(url, method, params = None, deleteCharacter = False):
	if(method == 'POST'):
		req = requests.post(url, headers = headers, cookies = cookies, params=params)
	else:
		req = requests.get(url, headers = headers, cookies = cookies, params = params)

	htmlDoc = str(req.text)
	if(deleteCharacter):
		htmlDoc = htmlDoc.replace('\n', '')
		htmlDoc = htmlDoc.replace('\t', '')
	return htmlDoc

def write(content):
	f = open('test.html', 'w', encoding = 'utf8')
	f.write(content)
	f.close()

def getString(page, number):
	url = "http://drugs.dxy.cn/dwr/call/plaincall/DrugUtils.showDetail.dwr"
	payload = {"callCount": "1", "page":"/drug/"+ page +".htm", "scriptSessionId":str(countID),\
"c0-scriptName":"DrugUtils", "c0-methodName":"showDetail", "c0-id":"0", "c0-param0":"number:"+ page, "c0-param1":"number:"+str(number),\
"batchId":str(countID)}
	content = getHtmlString(url, 'POST', params = payload)
	content = re.findall(r'<p>(.*?)</p>', content)
	stx = []
	cnt = 0
	for i in content:
		i = i.encode('latin-1').decode('unicode_escape')
		i = i.replace('<strong>', '')
		i = i.replace('</strong>', '')
		if cnt != 0:
			i = str(cnt) + '.' + '\n' + i
		cnt += 1
		stx.append(i)
	tring = '\n'.join(stx)
	return tring

def getData(url):
	titles = []
	content = getHtmlString(url, 'GET', deleteCharacter = True)
	text = BeautifulSoup(content, 'html.parser')
	x = text.find_all('span', class_ = 'fl')
	for i in x:
		titles.append( i.get_text() )

	x = re.findall(r'</dt>(.*?)<dt>', content)
	#write('\n'.join(x))
	ss = []
	for i in x:
		if 'br' in i:
			tring = '\n'.join( re.findall(r'>(.*?)<br/', i) )
			#print( re.findall( r'([\u4e00-\u9fa5]*?)<br/>', content) )
		elif 'login' in i:
			page, number = re.findall(r'<dd id="(.*?)">', i)[0].split('_')
			tring = getString(page, number)
		elif '<p>' in i:
			tring = '\n'.join( re.findall(r'<dd>(.*?)</dd>', i) )
			tring = tring.replace('<p>', '')
			tring = tring.replace('</p>', '\n') 
		else:
			tring = '\n'.join( re.findall(r'<dd>(.*?)</dd>', i) )

		ss.append(tring.strip())

			

	y = re.findall(r'<dd>(.*?)</dl>', content)[0]
	last = re.findall(r'<dd>(.*?)</dd>', y)[-1]
	ss.append( last.strip() )
	sys.exit(0)



def process(url):
	html = getHtmlString(url, 'GET')
	#获得总页数
	numPage = int( re.findall(r'span title="第1-10条, 共(.*?)页" class="current">', html)[0] )
	
	for page in range(1, numPage+1):
		params = {'page': page}
		content = getHtmlString(url, 'GET', params)
		urls = re.findall(r'<a href="(.*?).htm">.*?</a>',  content)
		for each in urls:
			if each[-1].isdigit():
				getData(each+'.htm')
				break
		break
		#f = open(str(page)+'.html', 'w', encoding = 'utf8')
		#f.write(content)


def main():
	#网址首页
	url = 'http://drugs.dxy.cn/'
	#获得目录
	html = getHtmlString(url, 'GET')
	links = re.findall(r'<h3><a href="(.*?)">.*?</a></h3>', html)
	#titles = re.findall(r'<h3><a href=".*?">(.*?)</a></h3>', html)
	#for i in range( len(links) ):
	#	print(links[i], titles[i])
	for link in links:
		process(link)
		break

main()

