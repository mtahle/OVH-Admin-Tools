import json
import ovh
from urllib import quote

client = ovh.Client()
with open('iplist.txt',"r") as input:
	ips = input.readlines()
	for ip in ips:
		try:
			result = client.delete('/ip/{}/reverse/{}'.format(quote(ip),quote(ip)))
			print json.dumps(result, indent=4)
		except:
			continue