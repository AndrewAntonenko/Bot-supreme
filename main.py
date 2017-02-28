import requests

clothes_name = 'Rigid Slim'
colour = 'Indigo'


domain = 'http://www.supremenewyork.com'
main_page = 'http://www.supremenewyork.com/shop/all/pants'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(main_page, headers = headers)

start = 4800

super_code = r.text

number = super_code.find(clothes_name, start)

number_end = super_code.find(colour, number)

number_href_begin = super_code.rfind('=', number, number_end) + 2

my_super_href_hui_govno = domain + super_code[number_href_begin:number_end-2]

print(my_super_href_hui_govno)



#Add to your basket

size = '34'
r = requests.get(my_super_href_hui_govno, headers = headers)
super_code = r.text

number = super_code.find('size')

number_end = super_code.find(size, number)

super_size = super_code[number_end-7:number_end-2]

number_end = super_code.rfind('value', 0, number)
super_style = super_code[number_end+7:number_end+12]

payload = {'utf8':'✓', 'style':17368, 'size':33267, 'commit':'add+to+basket'}

'''rr=requests.post(domain+"/shop/302253/add", data = payload)
print(rr.status_code, rr.reason)
print(rr.text)
page_cart = requests.get(domain+"/shop/cart", headers).text
#print(page_cart)

'''

import http.client
import urllib.parse
domain = 'www.supremenewyork.com'
params = urllib.parse.urlencode(payload)
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = http.client.HTTPConnection(domain+"/shop/302253/add")
conn.request("POST", "", params, headers)

response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
print(data)

conn.close()






'''
ss = page_clothes.find('button checkout')
sss = page_clothes.rfind(' id=\'cart', 0, ss)
#print(page_clothes[sss:])
'''


