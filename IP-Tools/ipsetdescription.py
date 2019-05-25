
import ovh
from urllib import quote

client = ovh.Client()
with open('iplist.txt',"r") as input:
	ips = input.readlines()
	for ip in ips:
		try:
    			status = client.put('/ip/{}'.format(quote(ip)), description='Mailer')
			print status
		except:
			print "Error"
			print status
			continue