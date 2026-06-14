"""
@Project: PythonProject
@File: unit_type.py
@Autor: pm
@Date: 2026/3/20
@Describe: 户型分布统计
"""
import re

import numpy as np
import pandas as pd

from hz_project.dataProcessing.amout_district import count, json_path

input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
json_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\unitTypeAmout.json"
with open(input_json, "r", encoding="utf-8") as infile:
    typelist = []
    amout_list = []
    for line in infile:
        line = line.strip()
        if not line:
            continue
        pairs = re.findall(pattern, line)
        # print(type(pairs))
        # unit_type
        # unit_type ={}
        data = pd.DataFrame(pairs)
        # print(data)
        unit_type = data.loc[1]
        for i in unit_type:
            typelist.append(i)

    unit_type_list = [x for x in typelist if x != "户型"]
    data = pd.DataFrame(unit_type_list, columns=["unit_type"])
    print(data.head(100))

    type_sum = pd.DataFrame(data["unit_type"].value_counts())
    counts = type_sum.groupby("unit_type")
    print("counts:", counts)
    unit_type_sum = {}
    a = 0
    for i in type_sum.head(10).itertuples():
        type_district = i[0]
        count = i[1]
        a += count
        unit_type_sum.update({type_district: count})
        # print(i)
        # print(f"{type_district}的数量为:{count}")
    print(a - 3520 - 1454 - 68 - 240)
    print("unit_type_sum:", unit_type_sum)
    out_data = pd.DataFrame([unit_type_sum])
    print("outdata:", out_data)
    out_data.to_json(json_path, orient="index", force_ascii=False, indent=4)
    print("数据保存成功")
