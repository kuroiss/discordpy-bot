from contextlib import nullcontext
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

page_num_list = ['335', '234', '13', '14', '15', '17', '18', '19', '436']

lower_level = 11

for i in range(lower_level, 20):
    # URLの指定
    url = 'https://w.atwiki.jp/asigami/'
    page_num = page_num_list[i - lower_level]
    
    url = url + 'pages/' + page_num + '.html'
        
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    
    # テーブルを指定
    table = bsObj.findAll('table')[2]
    
    rows = table.findAll('tr')
    
    with open('dance_'+str(i)+'.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)


            