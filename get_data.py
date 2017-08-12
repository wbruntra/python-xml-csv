import requests
from bs4 import BeautifulSoup
import csv

## Config
output_file = 'plants.csv'
delimiter = ','

remote = False
url = "https://www.w3schools.com/Xml/plant_catalog.xml"
local_file = 'plant_catalog.xml'

xml_item_name = 'PLANT'
columns = ['COMMON', 'LIGHT','PRICE']
##

if remote:
    page = requests.get(url).content
else:
    with open(local_file, 'rb') as f:
        page = f.read()
soup = BeautifulSoup(page, "xml")

items = soup.findAll(xml_item_name)

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=delimiter)
    writer.writerow(columns)
    for item in items:
        row = []
        for column in columns:
            try:
                row.append(item.find(column).string)
            except AttributeError:
                row.append('')
        writer.writerow(row)
