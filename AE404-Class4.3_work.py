import requests 
from bs4 import BeautifulSoup
import re

respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books")
soup = BeautifulSoup(respond.text,'html.parser')
divs = soup.find_all("div", class_ = "type02_bd-a")

amount = 0

a_tags = soup.find_all('a')

for url in a_tags:
    if re.fullmatch("https://www.books.com.tw/products/(\d+)/[?]loc=P_0003_(\d+)", url['href']) != None:
        print (url.text+':'+url['href'])
        with open(str(url.text)+"-"+url['href']+".jpg","r") as f:
            f.read()
    amount +=1
    if amount >4:
        break


'''
for url in divs.find_all('a',href = re.compile('[?]loc=P_0002_(\d+)')):
    print (url.text+':'+url['href'])
'''