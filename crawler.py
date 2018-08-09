# py

import requests
from bs4 import BeautifulSoup

url = 'http://www.imsdb.com/all%20scripts/'
r = requests.get(url)
content = BeautifulSoup(r.text, 'lxml')
urls = [i.a['href'] for i in content.find_all('p')]

urls = ['http://www.imsdb.com/scripts/'+ url.split('/')[2].replace(' Script', '').replace(' ', '-').replace(':', '') for url in urls]

for k, url in enumerate(urls):
    flushPrint(k)
    r = requests.get(url)
    content = BeautifulSoup(r.text, 'lxml')
    try:
        content = content.find_all('td', {'class', 'scrtext'})[0].text
        filename = 'imsdb/'+url.split('/')[-1].replace('html', 'txt')
        with open(filename, 'w') as f:
            f.write(content)
    except:
        print(k, url)
        pass
