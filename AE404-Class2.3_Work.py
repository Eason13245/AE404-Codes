import requests 
from bs4 import BeautifulSoup

res = requests.get("https://www.books.com.tw/web/sys_saletopb/books")

soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all("div", class_ = "type02_bd-a")
lis = soup.find_all("li",class_ = "item")

amount = 0



for index, each_div in enumerate(divs):
    h4 = each_div.find("h4")
    if not h4:
        continue
    a = each_div.find("a")
    if not a:
        continue
    bookName = a.text
    ul = each_div.find('ul',class_ = "msg")
    if not ul:
        continue
    lis2 = ul.find('li')
    if not lis2:
        continue
    aname =  lis2.find("a")
    if not aname:
        continue
    Aname = aname.text
    print ('排名'+str(index+1)+ ':'+bookName+"作者"+":"+str(Aname))
    for each_li in lis[:3]:
        img = each_li.find("img")
        src = img['src']
        alt = img['alt']
        imgR = requests.get(src)
        with open(str(index+1)+"-"+bookName+"-"+str(Aname),"rb") as f:
            f.write(imgR.content)
    amount += 1
    if amount >4:
        break


