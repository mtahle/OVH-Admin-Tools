import re
import json
import ovh
from urllib import quote

client = ovh.Client()
with open('iplist.txt',"r") as input:
	ips = input.readlines()
	for ip in ips:
		status = client.get('/ip/{}'.format(quote(ip)))
		print json.dumps(status, indent=4)
