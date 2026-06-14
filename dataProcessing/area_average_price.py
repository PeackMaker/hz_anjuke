"""
@Project: PythonProject
@File: area_average_price.py
@Autor: pm
@Date: 2026/3/20
@Describe: 区域均价统计
"""
import json
import re

import numpy as np
import pandas as pd
from numpy.ma.extras import average

input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
json_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\avgPriceAndArea.json"
with open(input_json, 'r', encoding='utf-8') as f:
    text = f.read()
    text = text.strip()
    re.findall(pattern, text)
    if not text.startswith('['): text = '[' + text + ']'
    data_list = json.loads(text)
    df = pd.DataFrame(data_list)
    # pd.set_option('display.max_rows', None)
    # print(df["所属区域"]=="杭州")
    # 提取区域列和均价列
    # 利用切片提取区域，去掉均价单位“万/m**2”
    # df["所属区域"] = df["所属区域"].apply(lambda x: x[0:5])
    df["所属区域"] = df["所属区域"].apply(lambda x: x[0:2] if not x[0:2]=="杭州" else np.nan)
    df["均价"] = df["均价"].apply(lambda x: x[0:-3]).astype(int)
    # df.info()
    df_new = df[["所属区域","均价"]].copy()
    # print(df_new)
    # print(df_new)
    group_area_price = df_new.groupby("所属区域")["均价"].mean().round(2)
    print(group_area_price)
    area_price = pd.DataFrame(group_area_price)
    group_area_price.to_json(json_path,orient='index',force_ascii=False,indent=4)
    # print(area_price)
    print("保存成功")
    for col in area_price.itertuples():
        area=col[0]
        average_price=col[1]
        print(f"{area}的均价是{average_price}元/m2")