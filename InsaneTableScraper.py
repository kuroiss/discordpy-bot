import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

for i in range(1, 26):
    # URLの指定
    html = urlopen('http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=search&type=insane&exlevel='+str(i)+'&7keys=1')
    bsObj = BeautifulSoup(html, 'html.parser')
    
    # テーブルを指定
    table = bsObj.findAll('table')[0]
    rows = table.findAll('tr')
    
    with open('insane_'+str(i)+'.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
            