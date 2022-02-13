import requests
from bs4 import BeautifulSoup # html資料的擷取

r=requests.get('https://disp.cc/b/PttHot')
root_url='https://disp.cc/b/'
soup= BeautifulSoup(r.text,'html.parser') #用parser解析text 像是unicode之類的

spans=soup.find_all('span',class_='listTitle') #get 指的是拿到class屬性
#for span in spans:

    # href=span.find('a').get('href')
    # if href=='796-eD9G':
    #       continue
    # url = root_url+href
    # title=span.text
    # print(f'{title}\n{url}')

for span in soup.select('span.listTitle'): #select 後面可以用css的寫法
    href = span.find('a').get('href')
    if href=='796-eD9G':
          continue
    url = root_url+href
    title=span.text
    print(f'{title}\n{url}')

