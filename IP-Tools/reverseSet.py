import ovh
from urllib import quote

client = ovh.Client()
with open('iplist.txt',"r") as input:
	ips = input.readlines()
	for ip in ips:
		try:
			status = client.post('/ip/{}/reverse'.format(quote(ip)),ipReverse=ip, reverse = '')
			print status
		except:
			#print "Error"
			#print status
			continue