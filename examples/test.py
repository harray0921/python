#! /usr/bin/python

import sys
import requests

html = requests.get("https://www.baidu.com")

def transformCodec(re_data):#ascii
    try:
	re_data = re_data.decode('gbk')
    except Exception as error:
	print error
	print 'delete illegal string,try again...'
	pos = re.findall(r'decodebytesinposition([\d+])-([\d]+):illeagal',str(error).replace(' ',''))
	if len(pos)==1:
	    re_data = re_data[0:int(pos[0][0])]+re_data[int(posp[0][1]):]
	    re_data = transformCode(re_data)
	    return re_data
	return re_data
print transformCodec(html.text)
