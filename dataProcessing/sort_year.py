"""
@Project: PythonProject
@File: sort_year.py
@Autor: pm
@Date: 2026/3/20
@Describe: 按年份统计
"""
import re
from traceback import format_list

import pandas as pd

input_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
json_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\amoutGroupYear.json"


with open(input_json) as f:
    pattern = re.compile(r'"(.*?)"\s*:\s*"(.*?)"')
    with open(input_json, "r", encoding="utf-8") as infile:
        yearlist = []
        for line in infile:
            line = line.strip()
            if not line:
                continue
            pairs = re.findall(pattern, line)
            # get year
            createYear = pairs[5][1][0:4]
            yearlist.append(createYear)
        df_year = pd.DataFrame(yearlist,columns=['year'])
        # print(df_year.head(10))
        year_count = pd.DataFrame(df_year["year"].value_counts()).sort_values(by='year')
        year_count.to_json(json_path, orient="index", force_ascii=False, indent=4)
        # print(year_count)
        for item in  year_count.itertuples():
            year = item[0]
            count = item[1]
            print(f"{year}年建造的小区数量为：{count}")



