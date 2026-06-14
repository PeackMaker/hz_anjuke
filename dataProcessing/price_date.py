"""
@Project: PythonProject
@File: price_date.py
@Autor: pm
@Date: 2026/3/21
@Describe: 均价和建造年份的关系
"""
import json
import re
from itertools import groupby

import pandas as pd
json_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\priceDate.json"
input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
with open(input_json,encoding="utf-8") as f:
    text=f.read()
    text =text.strip()
    re.findall(pattern, text)
    if not text.startswith('['): text = '[' + text + ']'
    data_list = json.loads(text)
    df = pd.DataFrame(data_list)
    #提取年份列和均价列
    df["时间"]=pd.to_datetime(df["时间"].apply(lambda x: x[0:4]),format="%Y").dt.year
    # df["时间"]=pd.to_datetime(df["时间"].apply(lambda x: x[0:4])).dt.strftime('%Y')
    # print(df["时间"])
    df["均价"] = df["均价"].apply(lambda x: x[0:-3]).astype(int)
    # print( df["均价"])
    # 整合新的dataframe
    df_date_average=df[["时间","均价"]].copy()
    group_date = df_date_average.groupby("时间")["均价"].mean().round(2)
    price_sort_date = pd.DataFrame(group_date).sort_values("时间", ascending=True)
    price_sort_date.to_json(json_path, orient="index", force_ascii=False, indent=4)
    print(price_sort_date)
    for col in price_sort_date.itertuples():
        date=col[0]
        average_price=col[1]

