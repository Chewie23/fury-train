import urllib2
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = 'https://jira.atlassian.com/'
EXP = 'https://jira.rim.net/'

#urllib2.urlopen(EXP, context=ctx)

username = 'achu'
password = 'something'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()

p.add_password(None, EXP, username, password)

handler = urllib2.HTTPBasicAuthHandler(p)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

page = urllib2.urlopen(EXP, context=ctx).read() #doesn't work anyway