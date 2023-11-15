from contextlib import nullcontext
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

lower_level = 40

for i in range(lower_level, 51):
    # URLの指定
    url = 'https://popn.wiki/' + '%E9%9B%A3%E6%98%93%E5%BA%A6%E8%A1%A8' + '/lv'
    
    url = url + str(i)
    
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    
    # テーブルを指定
    table = bsObj.findAll('table')[0]
    
    rows = table.findAll('tr')
    
    with open('popn_'+str(i)+'.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)


            