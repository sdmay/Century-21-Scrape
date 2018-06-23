import requests
from bs4 import BeautifulSoup
l=[]
base='https://www.century21.com/real-estate/tampa-fl/LCFLTAMPA/?p='
for i in range(1, 22):
#     print(base + str(i) +'in tbe looooooopppp')
    r=requests.get(base + str(i))
    c=r.content
    soup=BeautifulSoup(c, 'html.parser')
#     print(soup)
    all=soup.find_all('div', {'class':'property-card'})
#     print(all)
    for item in all:
#         print('loop')
        d={}
        try:
            d['Price']=(item.find('a', {'class':'listing-price'}).text.replace('\n', '').strip())
            d['Address']=(item.find('div',{'class':'property-address'}).text.replace('\n', '').strip())
            d['City']=(item.find('div',{'class':'property-city'}).text.replace('\n', '').strip())
        except:
            pass
        try:
            d['Beds']=('Beds ' + item.find('div',{'class':'property-beds'}).text.replace('\n', '').strip())
            d['Baths']=('Baths ' + item.find('div',{'class':'property-baths'}).text.replace('\n', '').strip())
        except:
            d['Beds']=None
            d['Baths']=None
            pass
        try:
            d['Half-Baths']=(item.find('div',{'class':'property-half-baths'}).text.replace('\n', '').strip())
        except:
            d['Half-Baths']=None
            pass
        try:
            d['Area']=(item.find('div',{'class':'property-sqft'}).text.replace('\n', '').strip())
        except:
            d['Area']=None
            pass

    #     print(d)
        l.append(d)

import pandas
print(l)

df=pandas.DataFrame(l)


df.to_csv('output.csv')
