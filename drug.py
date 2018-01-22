import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 

def getCookies(cookiesStr):
	cookies = {}
	for line in cookiesStr.split(';'):
		key, value = line.split('=', 1)
		key = key.strip()
		value = value.strip()
		cookies[key] = value
	return cookies


url = "http://drugs.dxy.cn/dwr/call/plaincall/DrugUtils.showDetail.dwr"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

cookiesStr  = "__asc=f3741e5a1611db7b8b2c587aa00; __auc=f3741e5a1611db7b8b2c587aa00; __utma=129582553.902107930.1516622036.1516622036.1516622036.1; __utmc=129582553; __utmz=129582553.1516622036.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.1400654000.1516622045; _gid=GA1.2.2101370569.1516622045; Hm_lvt_d1780dad16c917088dd01980f5a2cfa7=1516622035,1516622047; DRUGSSESSIONID=FC1CDC908410145E3C827187A832DAC7-n1; JUTE_BBS_DATA=1785c373cdecd3b4cac9959c1098b0966a862db3131885e26582573bce31235b4d15cb5d709620d8473552ef8365c2554f7feb390193ba3648825c60a03362764b18f206bee0b0141b45d122190ed6a8; __utmb=129582553.6.10.1516622036; Hm_lpvt_d1780dad16c917088dd01980f5a2cfa7=1516622157"
#cookiesStr = "__asc=f3741e5a1611db7b8b2c587aa00; __auc=f3741e5a1611db7b8b2c587aa00; __utma=129582553.902107930.1516622036.1516622036.1516622036.1; __utmc=129582553; __utmz=129582553.1516622036.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.1400654000.1516622045; _gid=GA1.2.2101370569.1516622045; Hm_lvt_d1780dad16c917088dd01980f5a2cfa7=1516622035,1516622047; DRUGSSESSIONID=FC1CDC908410145E3C827187A832DAC7-n1; JUTE_BBS_DATA=1785c373cdecd3b4cac9959c1098b0966a862db3131885e26582573bce31235b4d15cb5d709620d8473552ef8365c2554f7feb390193ba3648825c60a03362764b18f206bee0b0141b45d122190ed6a8; __utmt=1; __utmb=129582553.10.10.1516622036; Hm_lpvt_d1780dad16c917088dd01980f5a2cfa7=1516623775"
cookies = getCookies(cookiesStr)
payload = {"callCount": "1", "page":"/drug/94068.htm", "scriptSessionId":"76A4F2AFF35387DFE9C116FE32170A99907",\
"c0-scriptName":"DrugUtils", "c0-methodName":"showDetail", "c0-id":"0", "c0-param0":"number:94068", "c0-param1":"number:3",\
"batchId":"2"}
req = requests.post(url, headers = headers, cookies = cookies, params=payload)
htmlDoc = str(req.text)
print(htmlDoc)
f = open('drug.html', 'w', encoding = 'utf8')
f.write(htmlDoc)
f.close()

#print(req.content)

'''
callCount=1
page=/drug/94068.htm
httpSessionId=
scriptSessionId=76A4F2AFF35387DFE9C116FE32170A99907
c0-scriptName=DrugUtils
c0-methodName=showDetail
c0-id=0
c0-param0=number:94068
c0-param1=number:3
batchId=2
'''

'''
callCount=1
page=/drug/94068.htm
httpSessionId=
scriptSessionId=76A4F2AFF35387DFE9C116FE32170A99907
c0-scriptName=DrugUtils
c0-methodName=showDetail
c0-id=0
c0-param0=number:94068
c0-param1=number:14
batchId=3
'''



