import requests

clothes_name = 'Leather Work Jacket'
colour = 'Silver'

domain = 'http://www.supremenewyork.com'
main_page = 'http://www.supremenewyork.com/shop/all/jackets'
size = 'XLarge'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
start = 4800
number = -1



import datetime
while str(datetime.datetime.now().time())[0:8] < "00:00:00":
    pass

print(str(datetime.datetime.now().time())[0:8])

while number==-1:
    r = requests.get(main_page, headers = headers)
    super_code = r.text

    number = super_code.find(clothes_name, start)


number_end = super_code.find(colour, number)

number_href_begin = super_code.rfind('=', number, number_end) + 2

my_super_href_hui_govno = domain + super_code[number_href_begin:number_end-2]

#print(my_super_href_hui_govno)

#Add to your basket


r = requests.get(my_super_href_hui_govno, headers = headers)
super_code = r.text

number = super_code.find('size')

number_end = super_code.find(size, number)

super_size = super_code[number_end-7:number_end-2]

number_end = super_code.rfind('value', 0, number)
super_style = super_code[number_end+7:number_end+12]

payload = {'utf8':'✓', 'style':super_style, 'size':super_size, 'commit':'add+to+basket'}

rr = requests.session()
rr.post(domain+"/shop/302253/add", data = payload)
#print(rr.headers)
#print(rr.status_code, rr.reason, rr.headers)


#rrr = requests.session()
rrr = rr.get(domain+"/shop/cart")
#print(rrr.text)
rrr = rr.get(domain+"/checkout").text
authenticity_start = rrr.find('authenticity_token\" value=\"') + 27
auth_token = rrr[authenticity_start:authenticity_start+88]
#print(auth_token)

user_info = {
    "utf8":"✓",
    "authenticity_token":auth_token,
    "order[billing_name]":"Evgeniy+Medvedev",
    "order[email]":"fedor.chuprakov@mail.ru",
    "order[tel]":"+79091505477",
    "order[billing_address]":"Dybenko+st.+16+k+1+apartment+20",
    "order[billing_address_2]":"",
    "order[billing_address_3]":"",
    "order[billing_city]":"Moscow",
    "order[billing_zip]":"125475",
    "order[billing_country]":"RU",
    "same_as_billing_address":"1",
    "store_credit_id":"",#This must be left empty
    "credit_card[type]":"master",
    "credit_card[cnb]":"5469+3800+5519+2081",
    "credit_card[month]":"10",
    "credit_card[year]":"2021",
    "credit_card[vval]":"369",
    #"order[terms]":"0",
    "order[terms]":"1",
    "hpcvv":""
}

result = rr.post(domain+"/checkout", data=user_info)
print(str(datetime.datetime.now().time())[0:8])

print(result.text)
#print(rrr.status_code, rrr.reason,rrr.headers)

#print(rrr.headers['Set-Cookie'])






