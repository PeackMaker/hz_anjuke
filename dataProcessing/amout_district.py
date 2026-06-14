"""
@Project: PythonProject
@File: amout_district.py
@Autor: pm
@Date: 2026/3/20
@Describe: 各小区房源数量统计,按["所属小区"]统计
"""

import re

import pandas as pd

input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
json_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\amoutAndArea.json"

districtDit = {}
with open(input_json, "r", encoding="utf-8") as infile:
     for line in infile:
        l = []
        line =line.strip()
        if not line:
            continue
#         """
#         get keys: values
#         [("标题",""),("户型",""),("方位","")......]
#         """
        pairs = re.findall(r'"(.*?)"\s*:\s*"(.*?)"', line)
        data = pairs[6][1]
        if data not in districtDit:
            districtDit[data]= 1
        else:
            districtDit[data] += 1
districtDit =sorted(districtDit.items(), key=lambda x: x[1], reverse=True)
print(districtDit)
comms = pd.DataFrame(districtDit,columns=["name","count"])
comms.to_json(json_path,orient="index",force_ascii=False,indent=4)
print(comms)

# 输出
for item in comms.head(10).itertuples():
    name= item[1]
    count= item[2]
    print(f"{name}有:\t{count}套房源")