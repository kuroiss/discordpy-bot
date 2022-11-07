from contextlib import nullcontext
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

for i in range(11, 13):
    # URLの指定
    url = 'https://w.atwiki.jp/bemani2sp/'
    page_num = '14'
    if i == 12:
        page_num = '17'
        
    url = url + 'pages/' + page_num + '.html'
        
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    
    # テーブルを指定
    table = bsObj.findAll('table')[0]
    rows = table.findAll('tr')
    
    with open('beat_'+str(i)+'.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)


            