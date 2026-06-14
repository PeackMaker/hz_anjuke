"""
@Project: PythonProject
@File: clean_data.py
@Autor: pm
@Date: 2026/3/17
@Describe: clean the data spider from HZ_AJK
"""
import collections
import re
import json
from collections import Counter

import pandas as pd

'''
{"标题": "樱花大道旁 一线江景房  精装修 拎包入住送20方大露台", "户型": "2 室 2 厅 2 卫", "面积": "130.93㎡", "方位": "东南", "楼层": "中层(共32层)", "时间": "2008年建造", "所属小区": "观邸国际", "所属区域": "滨江钱江湾新和路167号", "总价": "380 万 ", "均价": "\n                    29024元/㎡\n                ", "房龄": "2年内"},
非标准json格式，这里不用正则写
'''


# 处理json文件找到重复键值对，统计重复次数
def findDuplicates(input_json):
    values = []
    with open(input_json, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            # 如果行尾有逗号，去掉
            if line.endswith(","):
                line = line[:-1]
            if not line:
                continue
            try:
                data = json.loads(line)
                # 清洗数据：把里面均价换行符去掉统一格式
                if "均价" in data:
                    data["均价"] = data["均价"].strip().replace("\n", "").replace(" ", "")
                    # 转成字符串存进去
                    values.append(json.dumps(data, ensure_ascii=False, sort_keys=True))
            except json.decoder.JSONDecodeError as e:
                print(f"解析失败：{line}，错误：{e}")
                continue
    counts = collections.Counter(values)
    dup_count = 0
    unique_count = 0
    for val, count in counts.items():
        if count > 1:
            item = json.loads(val)
            print(f"'{item.get('标题')}'重复了： {count}次")
            dup_count += 1
        else:
            unique_count += 1
    print(f"共有{len(values)}条有效数据")
    print(f"重复的数据有'{dup_count}'个类型(共{sum(c for c in counts.values() if c > 1)})条")
    print(f"不重复的数据有'{unique_count}'条")


def cleanData(input_json, output_json, output_excel):
    """
    处理json文件，去除重复键值对/换行符/空格
    并将清洗后的数据写到json文件或者excel文件
    :param input_json:
    :param output_json:
    :param output_excel:
    :return:
    """
    seen_titles = set()
    cleaned_data = []
    # pattern = re.compile(r'[\s\r\n\u3000]+')

    with open(input_json, 'r', encoding='utf-8') as infile, \
         open(output_json, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            print(len(line))
            # 提取所有键值对
            pairs = re.findall(r'"(.*?)"\s*:\s*"(.*?)"', line)

            if not pairs:
                continue

            # 拿出标题作为判断是否重复的依据
            title = pairs[0][1]
            if title in seen_titles:
                continue  # 重复标题，跳过
            seen_titles.add(title)

            cleaned_pairs = []
            record_dict = {}

            for key, value in pairs:
                if key == '标题':
                    cleaned_value = value
                else:
                    cleaned_value = value.replace('\\n', '') \
                                         .replace('\n', '') \
                                         .replace('\r', '') \
                                         .replace(' ', '') \
                                         .replace('\u3000', '')
                cleaned_pairs.append(f'"{key}": "{cleaned_value}"')
                record_dict[key] = cleaned_value

            # 写入清洗后的行
            cleaned_line = '{' + ', '.join(cleaned_pairs) + '},'
            outfile.write(cleaned_line + '\n')
            cleaned_data.append(record_dict)

    # 写入 Excel 文件
    if output_excel:
        df = pd.DataFrame(cleaned_data)
        df.to_excel(output_excel, index=False)

    # seen_titles = set()
    # cleaned_data = []
    #
    # with open(input_json, 'r', encoding='utf-8') as infile, \
    #         open(out_json, 'w', encoding='utf-8') as outfile:
    #
    #     for line in infile:
    #         line = line.strip()
    #         if not line:
    #             continue
    #
    #         # 提取所有键值对
    #         pairs = re.findall(r'"(.*?)"\s*:\s*"(.*?)"', line)
    #
    #         if not pairs:
    #             continue
    #
    #         # 拿出标题作为判断是否重复的依据
    #         title = pairs[0][1]
    #         if title in seen_titles:
    #             continue  # 重复标题，跳过
    #         seen_titles.add(title)
    #
    #         cleaned_pairs = []
    #         record_dict = {}
    #
    #         for key, value in pairs:
    #             if key == '标题':
    #                 cleaned_value = value
    #             else:
    #                 cleaned_value = value.replace('\\n', '') \
    #                     .replace('\n', '') \
    #                     .replace('\r', '') \
    #                     .replace(' ', '') \
    #                     .replace('\u3000', '')
    #             cleaned_pairs.append(f'"{key}": "{cleaned_value}"')
    #             record_dict[key] = cleaned_value
    #
    #         # 写入清洗后的行
    #         cleaned_line = '{' + ', '.join(cleaned_pairs) + '},'
    #         outfile.write(cleaned_line + '\n')
    #         cleaned_data.append(record_dict)
    #
    # # 写入 Excel 文件
    # if output_excel:
    #     df = pd.DataFrame(cleaned_data)
    #     df.to_excel(output_excel, index=False)


def main(input_json, output_json, output_excel):
    """
    调用去重和清洗函数
    :param input_json:
    :param output_json:
    :param output_excel:
    :return:
    """
    # 查重复数据
    findDuplicates(input_json)
    # 清洗数据并且去重
    cleanData(input_json, output_json, output_excel)
    print(f'清洗后的数据已保存到{output_json}和{output_excel}')


if __name__ == '__main__':
    input_json = "E:\pythonProjects\PythonProject\hz_project\data\originalData\data.json"
    out_json = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.json"
    out_excel = "E:\pythonProjects\PythonProject\hz_project\data\cleanData\data.xlsx"
    main(input_json, out_json, out_excel)
