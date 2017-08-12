import requests
from bs4 import BeautifulSoup
import csv

## Config
output_file = 'plants.csv'
delimiter = ','

remote = True
url = "https://www.w3schools.com/Xml/plant_catalog.xml"
local_file = 'plant_catalog.xml'

xml_item_name = 'PLANTS'
columns = ['COMMON', 'LIGHT','PRICE']
##

if remote:
    page = requests.get(url).content
else:
    with open(local_file, 'rb') as f:
        page = f.read()

soup = BeautifulSoup(page, "xml")
plants = soup.findAll(xml_item_name)

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=delimiter)
    writer.writerow(columns)
    for plant in plants:
        row = []
        for column in columns:
            row.append(plant.find(column).string)
        writer.writerow(row)
