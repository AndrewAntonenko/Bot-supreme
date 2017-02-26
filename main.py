'''import functions

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", int(n / x))
            break
    else:
        print(n, "is a prime number")

print(functions.ask_ok("Ну че бля пизда тебе или нет?\n"))


def fprintf(file, format, *args):
    file.write(format % args[0])

fprintf(open("1.txt", "w"),5,2,1,4)


'''

import lxml.html as html
from pandas import DataFrame
import requests

clothes_name = "Field Hooded"
colour = "Navy"


domain = "http://www.supremenewyork.com"
main_page = "http://www.supremenewyork.com/shop/all/sweatshirts"
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(main_page, headers = headers)

start = 4800

super_code = r.text

number = super_code.find(clothes_name, start)

number_end = super_code.find(colour, number)

number_href_begin = super_code.rfind("=", number, number_end) + 2

my_super_href_hui_govno = domain + super_code[number_href_begin:number_end-2]

print(my_super_href_hui_govno)



#Add to your basket
size = "34"
r = requests.get(my_super_href_hui_govno, headers = headers)
super_code = r.text
number = super_code.find("size")

number_end = super_code.find(size, number)
number_href_begin = super_code.rfind("=", number, number_end) + 2

print(super_code[number_href_begin:number_end-2])





#print(str(r))
#e = main_page.getroot().\
