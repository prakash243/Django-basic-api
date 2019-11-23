import urllib
from urllib import request
from urllib import response

resp = request.urlopen('https://www15.trakntell.com/tnt/servlet/tntAPI?orgid=083fdecea16a486519650060568865f2')

print(resp.read())
