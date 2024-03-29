#!/usr/bin/env python3

import requests
import bs4
import os
import json
from collections import OrderedDict
from datetime import datetime
import urllib3

url = 'https://www.benzinpreis-aktuell.de/tanken-esso-tankstelle-kehl-77694-92ef.html'
jsonFile = '/home/pi/Projets/python/pySpider-prix-carbu-de/data.json'

# add param

# add "verify=False" to resolve "OpenSSL.SSL.Error"
# add "urllib3" line to disable SSL connection warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get(url, verify=False)

soup = bs4.BeautifulSoup(response.text, "html.parser")

# two tag named "e-ps e-top24", select the second one which has the wanted information
# update [1] is not working anymore, change to [0]
# foundClass = str(soup.findAll(attrs={"class":"e-ps e-top24"})[1])
foundClass = str(soup.findAll(attrs={"class":"e-ps e-top24"})[0])
# print(foundClass)

wordSplit = foundClass.split()
# print(wordSplit)

dict_data = OrderedDict() 
dict_data ['date'] = 'default-date'
dict_data ['hour'] = 'default-hour'
dict_data ['price-95'] = 'default-price-95'
dict_data ['price-E10'] = 'default-price-E10'
dict_data ['price-diesel'] = 'default-price-diesel'

# dict_data['date'] = datetime.strptime("wordSplit[ wordSplit.index('dem') +1 ]", "%d.%m.%Y")
dict_data['date'] = wordSplit[ wordSplit.index('dem') +1 ]
# dict_data['hour'] = datetime.strptime("wordSplit[ wordSplit.index('um') +1 ]", "%H")
dict_data['hour'] = wordSplit[ wordSplit.index('um') +1 ]
dict_data['price-95'] = float(wordSplit[ wordSplit.index('Euro.') -1 ])
dict_data['price-E10'] = float(wordSplit[ wordSplit.index('Euro') -1 ])
dict_data['price-diesel'] = float(wordSplit[ wordSplit.index('€') -1 ])

with open(jsonFile, 'a') as fp:
    json.dump(dict_data, fp, sort_keys=True, indent=4)

print(dict_data['date'], dict_data['hour'], dict_data['price-95'], dict_data['price-E10'], dict_data['price-diesel'])
