from urllib import quote
import ovh

client = ovh.Client()
with open('iplist.txt', "r") as input:
    ips = input.readlines()
    for ip in ips:
        status = client.get('/ip/{}'.format(quote(ip)))
        if status['routedTo']['serviceName'] != 'ns541860.ip-144-217-254.net':
            print 'Moving IP ' + ip
            result = client.post('/ip/{}/move'.format(quote(ip)), nexthop=None, to='ns541860.ip-144-217-254.net')

            # Pretty print
            print 'IP: ' + ip + ' is moving'
        else:
            print 'The IP: ' + ip + ' is already there!'
