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

#print(r.headers)

#Add to your basket

size = '34'
r = requests.get(my_super_href_hui_govno, headers = headers)
super_code = r.text

number = super_code.find('size')

number_end = super_code.find(size, number)

super_size = super_code[number_end-7:number_end-2]

number_end = super_code.rfind('value', 0, number)
super_style = super_code[number_end+7:number_end+12]

payload = {'utf8':'✓', 'style':'17368', 'size':'33267', 'commit':'add+to+basket'}
print(r.status_code, r.reason, r.headers)

rr = requests.session()
rr.post(domain+"/shop/302253/add", data = payload)
print(rr.headers)
#print(rr.status_code, rr.reason, rr.headers)


#rrr = requests.session()
rrr = rr.get(domain+"/shop/cart")
print(rrr.text)
#print(rrr.status_code, rrr.reason,rrr.headers)

#print(rrr.headers['Set-Cookie'])






