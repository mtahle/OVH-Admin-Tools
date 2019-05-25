
import ovh
import json
client = ovh.Client()
with open('iplist.txt',"r") as input:
	ips = input.readlines()
	for ip in ips:
		try:
			result = client.post('/dedicated/server/ns541860.ip-144-217-254.net/virtualMac/02:00:00:8f:dd:59/virtualAddress',ipAddress=ip,virtualMachineName='Mailer')
			print json.dumps(result, indent=4)

		except AssertionError as error:
			print(error)
			continue