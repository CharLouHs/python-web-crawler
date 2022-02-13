import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.dcard.tw/f/food/p/228160071')
#root_url='https://disp.cc/b/'
soup= BeautifulSoup(r.text,'html.parser')
#spans=soup.find('div data-key').get('comment')
spans=soup.find_all('div',class_='sc-71lpws-1 hcbtbx-0 ekBGRs czZXCz')
data={}
nn=[]
cc=[]
for span in spans:
    try:
        name = span.find('span',class_='cax7qe-2 hKAjCB').text
        content = span.find('div',class_='phqjxq-0 iJJmxb').text

        if name in data:
            data[name].append(content)
        else:
            data[name]=[content]
        #data.update({name:content})
    except AttributeError:
        continue

for d in data:
    print(f"{d} 總留言數{len(data[d])}\n{data[d]}")

#print(k)
#print(f'{name}\n{content}')
# #print(f'{name}\n{content}')
        #nn.append(name)
        #cc.append(content)