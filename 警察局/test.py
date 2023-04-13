# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 03:34:28 2023

@author: fanzhen
"""

import json
import csv

with open('file.json', 'r') as f:
    data = json.load(f)

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'address', 'tel', 'longitude', 'latitude'])

with open('file.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for poi in data['pois']:
        name = poi['name']
        address = poi['address']
        tel = poi['tel']
        longitude, latitude = poi['location'].split(',')
        writer.writerow([name, address, tel, longitude, latitude])
