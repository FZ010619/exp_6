# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 03:14:00 2023

@author: fanzhen
"""

import requests
import json

url = "https://restapi.amap.com/v3/place/text"
params = {
    "types": "公安警察",
    "city": "晋源区",
    "offset": 20,
    "page": 1,
    "key": "d16f1979bc6ae61b78070e58b0507fe4",
    "extensions": "all",
    "output": "json",
    "fields": "address,name,adname,location,tel"
}

results = []
while True:
    response = requests.get(url, params=params)
    data = response.json()
    results.extend(data["pois"])
    if len(data["pois"]) < 20:
        break
    params["offset"] += 20
    params["page"] += 1

# 输出结果总数
print("共找到{}个公安警察部门".format(len(results)))

# 将结果保存为JSON文件
with open("晋源区.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False)

print("结果已保存.json中")
