from contextlib import nullcontext
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

level_limit_lower = 9

# 7, 8, 9, 10, 11, 12, Legendaria
pages = ["523", "512", "457", "270", "14", "17", "3246"]

for i in range(level_limit_lower, 14):
    # URLの指定
    url = 'https://w.atwiki.jp/bemani2sp/'
    page_num = pages[i - level_limit_lower]
    # page_num = "3246"
    
    url = url + 'pages/' + page_num + '.html'
        
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    
    # テーブルを指定
    table_index = 0 if i != 13 else 6
    table = bsObj.findAll('table')[table_index]

    rows = table.findAll('tr')
    
    with open('beat_'+str(i)+'.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)


            