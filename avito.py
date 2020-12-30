#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import requests
from bs4 import BeautifulSoup
import csv

with open('avito.csv', 'w', newline='', encoding='utf-8') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            datawriter.writerow(['Title']+['Year']+['Status']+['Price']+['Date']+['URL'])

r = requests.get('https://www.avito.ru/stavropol/avtomobili')

soup = BeautifulSoup(r.text, 'html.parser')
trade_list = soup.find_all('div', {'class': 'item_table-wrapper'})

for i in trade_list:
    name = i.find('a', {'class': 'snippet-link'})['title']
    url = 'https://www.avito.ru/' + i.find('a', {'class': 'snippet-link'})['href'] 
    date = i.find('div', {'class': 'snippet-date-info'})['data-tooltip']
    print(name, ',', url, ',', date, '\n-'*2)

    with open('avito.csv', 'a', newline='', encoding='utf-8') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            datawriter.writerow([name]+[date]+[url])



