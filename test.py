import http.client
import urllib.parse

params = urllib.parse.urlencode(
    {'utf8': '✓', 'style': 17368, 'size': 33267, 'commit': 'add+to+basket'}
)
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = http.client.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
print(data)

conn.close()