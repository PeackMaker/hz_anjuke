"""
@Project: PythonProject
@File: size_price.py
@Autor: pm
@Date: 2026/3/21
@Describe: 面积和均价的关系
"""
import re
import pandas as pd
import json
input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
json_path="E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\sizeAveragePrice.json"
pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
with open(input_json,encoding="utf-8") as f:
    text = f.read()
    text = text.strip()
    re.findall(pattern, text)
    if not text.startswith('['): text='['+text + ']'
    data_list = json.loads(text)
    df = pd.DataFrame(data_list)
    # 提取面积列和均价列
    df["面积"]= df["面积"].apply(lambda  x: x[0:-2]).astype(float)
    # print( df["面积"])
    df["均价"] = df["均价"].apply(lambda x:x[0:-3]).astype(int)
    # print(df["均价"])
    # 构建面积和均价dataframe
    size_average_price = df[["面积","均价"]].copy()
    # print(size_average_price)
    size_average_price.to_json(json_path,orient='index',force_ascii=False,indent=4)
    print("保存成功")
