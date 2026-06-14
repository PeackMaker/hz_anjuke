
"""
@Project: PythonProject
@File: price_group.py
@Autor: pm
@Date: 2026/3/21
@Describe: 房价区间统计
"""
import json
import re

import pandas as pd

from hz_project.dataProcessing.amout_district import count

input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
json_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\priceGroupAmout.json"
pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
with open(input_json,encoding="utf-8") as f:
    text = f.read()
    text = text.strip()
    re.findall(pattern, text)
    if not text.startswith('['): text = '[' + text + ']'
    data_list = json.loads(text)
    df = pd.DataFrame(data_list)
    # print(df.head())
    df["总价"]=df["总价"].apply(lambda x: x[0:-1]).astype(float)*10000
    # new_df = pd.DataFrame(df["总价"].copy())
    # print(new_df.head(100))
    # 分桶
    bins = [0,2000000,3000000,4000000,5000000,6000000,7000000,8000000,200000000000]
    labels =['200万以下', '200-300万', '300-400万', '400-500万', '500-600万', '600-700万','700-800万',"800万以上"]
    #构建分组对象
    price_groups = pd.cut(df["总价"],bins=bins,labels=labels)
    df["总价"]=price_groups
    pd.set_option("display.max_rows", None)
    new_df = pd.DataFrame(price_groups)
    # print(new_df.head(200))
    counts = df["总价"].value_counts()
    out = pd.DataFrame(counts)
    print(out)
    out.to_json(json_path,orient='index',force_ascii=False,indent=4)
    print("输出json文件")
    for item in out.itertuples():
        price_size = item[0]
        amout = item[1]
        print(f"{price_size}有{amout}套房")