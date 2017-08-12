import requests
from bs4 import BeautifulSoup
import csv

def read_file(name):
    with open(name, 'rb') as f:
        result = f.read()
    return result

## Config
output_file = 'plants.csv'
delimiter = ','

remote = True
url = "https://www.w3schools.com/Xml/plant_catalog.xml"
local_file = 'plant_catalog.xml'

xml_item_name = 'PLANT'
columns = ['COMMON', 'LIGHT','PRICE']
##

page = (requests.get(url).content if remote else
        read_file(local_file))

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
