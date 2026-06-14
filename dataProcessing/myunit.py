"""
@Project: PythonProject
@File: myunit.py
@Autor: pm
@Date: 2026/3/21
@Describe: 工具，提取json键值转成列表
"""
import json
import re

import pandas as pd

from hz_project.dataProcessing.sort_year import yearlist, input_json

# input_json = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\amoutGroupYear.json"
#
# with open(input_json, "r", encoding="utf-8") as f:
#     data_list = json.load(f)
#     print(data_list)
#     data = pd.DataFrame(data_list).T
#     print(data)
#     listOfYear = []
#     ListOfAmout = []
#     for data in data.itertuples():
#         listOfYear.append(data[0])
#         ListOfAmout.append(data[1])
#     print(listOfYear)
#     # print(type(listOfYear))
#     print(ListOfAmout)
#     newListOfYear = [item +"年" for item in listOfYear ]
#     print(newListOfYear)

# input_json = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\priceDate.json"
#
# with open(input_json, "r", encoding="utf-8") as f:
#     data_list = json.load(f)
#     print(data_list)
#     data = pd.DataFrame(data_list).T
#     print(data)
#     listOfYear = []
#     ListOfAveragePrice = []
#     for data in data.itertuples():
#         listOfYear.append(data[0])
#         ListOfAveragePrice.append(data[1])
#     newListOfYear = [item +"年" for item in listOfYear]
#     print(newListOfYear)
#     print(ListOfAveragePrice)

input_json = "E:\\pythonProjects\\PythonProject\\hz_project\\dataVisualization\\data\\sizeAveragePrice.json"
with open(input_json, "r", encoding="utf-8") as f:
    data_list = json.load(f)
    data = pd.DataFrame(data_list).T
    print(data)
    size_list = []
    avg_price_list = []
    for item in data.itertuples():
        size_list.append(item[1])
        avg_price_list.append(item[2])
    print(size_list)
    print(avg_price_list)