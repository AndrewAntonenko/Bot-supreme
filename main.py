'''import functions

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', int(n / x))
            break
    else:
        print(n, 'is a prime number')

print(functions.ask_ok('Ну че бля пизда тебе или нет?\n'))


def fprintf(file, format, *args):
    file.write(format % args[0])

fprintf(open('1.txt', 'w'),5,2,1,4)


'''

import lxml.html as html
from pandas import DataFrame
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

rr=requests.post(my_super_href_hui_govno, data = payload)
print(rr.status_code, rr.reason)
page_clothes = requests.get(my_super_href_hui_govno, headers).text

ss = page_clothes.find('button checkout')
sss = page_clothes.rfind(' id=\'cart', 0, ss)
#print(page_clothes[sss:])
