"""
@Project: PythonProject
@File: dataAnnlysis.py
@Autor: pm
@Date: 2026/3/21
@Describe: 数据预处理
"""
import joblib
import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from setuptools.sandbox import save_path
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号


def data_processing(xlsx_path):
    pd.get_option('display.max_columns')
    df = pd.read_excel(xlsx_path)
    # load file
    df = pd.read_excel(xlsx_path)
    # 数据清洗和转换
    # 处理缺失值和重复值
    df = df.dropna().drop_duplicates()
    # print(df.info)
    # 编码分类变量
    le = LabelEncoder()

    # 户型  转为 房间数 客厅数  卫生间数
    df[['房间数', '客厅数', '卫生间数']] = df["户型"].str.extract(r"(\d+)室(\d+)厅(\d+)卫").fillna(0).astype(int)
    # 面积
    df["面积"] = df["面积"].str.replace("㎡", '').astype(float)
    # 总价
    df["总价"] = df["总价"].str.replace("万", '').astype(float) * 10000
    # 均价
    df["均价"] = df["均价"].str.extract(r"(\d+)元").astype(float)
    # 建造年份
    df["建造年份"] = df["时间"].str.extract(r"(\d{4})年建造")[0].astype(int)
    # 楼层和楼层编码
    '''
     高层 2
     中层 0
     低层 1
     Nan  3
    '''
    df["楼层类别"] = df["楼层"].str.extract(r"([低中高]层)")[0]
    df["楼层编码"] = le.fit_transform(df["楼层类别"])
    df["总楼层"] = df["楼层"].str.extract(r"共(\d+)层")[0].astype(float)

    # 区域 区域编码
    '''
上城区：310000（含原江干区部分区域）
拱墅区：310000（含原下城区、拱墅区合并区域）
西湖区：310000（全区通用，部分街道如转塘为310024）
滨江区：310000（全区通用，浦沿街道为310053）
萧山区：311200（城区及大部分街道）
余杭区：311100（西部区域，如未来科技城、五常街道）
临平区：311100（原余杭区东部，如临平街道）
钱塘区：311200（含下沙、大江东区域，下沙街道为310018）
富阳区：311400
临安区：311300
桐庐县：311500
淳安县：311700
建德市：311600
    '''
    hz_codes = ["上城区", "拱墅区", "西湖区", "滨江区", "萧山区", "余杭区", "临平区", "钱塘区", "富阳区",
                "临安区", "桐庐县", "淳安县", "建德市"
                ]

    def extract_region(region):
        for district in hz_codes:
            if district[:2] in region:
                return district
        return "其它"

    df["区域"] = df["所属区域"].apply(extract_region)
    df["区域编码"] = le.fit_transform(df["区域"])

    # 房龄  房龄编码
    ''''
    2年内     1
    2-5 年       0
    '''
    house_life = ["2年内", "2-5年"]

    def extract_house_life(year):
        for district in house_life:
            if district in year:
                return district
        return "其它"

    df["房龄"] = df["房龄"].apply(extract_house_life)
    df["房龄编码"] = le.fit_transform(df["房龄"])

    # 方位 方位编码
    '''
    方位  方位编码
    0     南     5
    1    南北     6
    8    东西     3
    34   西南     9
    38   东南     2
    41   西北     8
    72    东     0
    84   东北     1
    96    北     4
    101   西     7
    '''
    df["方位编码"] = le.fit_transform(df["方位"])

    # 删除不需要的列
    df = df.drop(['标题', '方位', '户型', '楼层', '时间', '所属小区', '所属区域', '楼层类别', '房龄', '区域'], axis=1)

    # 调整列顺序
    df = df[['面积', '方位编码', '区域编码', '总价', '均价', '房间数', '客厅数', '卫生间数', '建造年份', '楼层编码',
             '总楼层', '房龄编码']]
    # 保存清洗后的数据
    df.to_excel("E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\cleanedData.xlsx", index=False)
    print("数据预处理完成，已经将结果保存到excel中")
    return df


def data_visualization(preprocessed_path):
    '''
    数据可视化函数
    :param preprocessed_path:
    :return:
    '''
    df = pd.read_excel(preprocessed_path)
    # 探索性数据分析
    # 绘制数值特征分布
    plt.figure(figsize=(20, 16))
    for i, col in enumerate(['面积', '总价', '均价', '建造年份',
                             '总楼层', '楼层编码', '方位编码', "区域编码"], 1):
        plt.subplot(4, 2, i)
        sns.histplot(df[col], kde=True)
        plt.title(f" {col}分布")
        if col == "均价":
            plt.xlim(0, 20000)
        if col == "总价":
            plt.xlim(0, 2500000)
        if col == "总楼层":
            plt.xlim(0, 50)
        if col == "楼层编码":
            plt.xticks(ticks=np.arange(0, 4), labels=["低层", "中层", "高层", "未知"])
        if col == "方位编码":
            plt.xticks(ticks=np.arange(0, 10),
                       labels=['东', '东北', '东南', '东西', '北', '南', '西', '西北', '西南', '未知'])
        if col == "区域编码":
            plt.xticks(ticks=np.arange(0, 13),
                       labels=["上城区", "拱墅区", "西湖区", "滨江区", "萧山区", "余杭区", "临平区", "钱塘区", "富阳区",
                               "临安区", "桐庐县", "淳安县", "建德市"])
    plt.tight_layout()
    plt.savefig("E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\值特征分布.png")
    plt.close()
    # print("数值特征值已保存")

    # 相关热力图
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("特征相关性热力图")
    plt.savefig("E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\特征相关性热力图.png")
    plt.close()
    print("特征相关热力图已保存")


def data_analysis_model(preprocessed_path):
    '''
    :argument preprocessed_path:
    :return:
    数据分析建模
    现在要看的是面积/方位编码/...对房价的影响
    '''
    df = pd.read_excel(preprocessed_path)
    # 特征和目标变量
    fetures = ['面积', '方位编码', '区域编码', '房间数', '客厅数', '卫生间数', '建造年份', '楼层编码', '总楼层',
               '房龄编码']
    target = ["总价"]
    x = df[fetures]
    y = df[target]

    # 填补缺失值,以均值填充
    fill_value = SimpleImputer(strategy='mean')
    x = fill_value.fit_transform(x)

    # 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # 标准化特征
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # 保存标准化器
    joblib.dump(scaler, "E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\scaler.pkl")
    print("保存标准化器")

    # 定义模型(随机森林回归模型)
    model = RandomForestRegressor(random_state=42)
    # 训练和评估模型
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("R2:", r2_score(y_test, y_pred))

    # 保存模型
    joblib.dump(model, "E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\model.pkl")
    print("模型已保存")


def price_future_predict(sclaer, model, preprocessed_path, years, png_save_path):
    '''
    预测未来几年房价趋势
    :param sclaer:
    :param model:
    :param preprocessed_path:
    :param years: 预测的年数
    :param png_save_path:
    :return:
    '''
    df = pd.read_excel(preprocessed_path)
    # 特征字段表，要与训练时模型保持一致
    features = ['面积', '方位编码', '区域编码', '房间数', '客厅数', '卫生间数', '建造年份', '楼层编码', '总楼层',
                '房龄编码']
    # 以各特征的中位数构造一个"典型样本"，用来预测未来趋势
    base_sample = df[features].median().values.reshape(1, -1)
    print(base_sample)
    print(base_sample.shape)
    print(base_sample.tolist())
    # print(type(base_sample))
    # 存储未来年份和房价
    future_years = []
    predict_prices = []
    for i in range(years):
        '''
        1 拷贝典型样本，逐年调整特征
        2 建造年份每年递增
        3 房龄编码每年递减
        4 总楼层每年变化（每3年加一层）
        5 标准化特征，保持与训练时一致
        6 用训练好的模型预测房价
        7 记录年份和预测结果
        
        '''
        # 1
        modified_sample = base_sample.copy()
        # 2
        modified_sample[0][features.index("建造年份")] += i
        # 3
        modified_sample[0][features.index("房龄编码")] = max(0, modified_sample[0][features.index("房龄编码")] - i)
        # 4
        modified_sample[0][features.index("总楼层")] += i % 3
        # 5
        scaled_sample = sclaer.transform(modified_sample)
        # 6
        predict_price = model.predict(scaled_sample)[0].round(2)
        print("predict_price:",predict_price)
        # 7
        future_years.append(2026 + i)
        predict_prices.append(predict_price)

    print("predict_prices:",predict_prices)

    # 绘制未来房价趋势图
    plt.figure(figsize=(10, 6))
    plt.plot(future_years, predict_prices, marker='o', linestyle='-', color='blue')
    # 取消y轴因数字过大转换的科学计数法
    plt.ticklabel_format(style="plain",axis="y")
    plt.xlabel("年份")
    plt.ylabel("预测房价(元)")
    plt.savefig(png_save_path)
    plt.title("未来{}年房价预测趋势".format(years))
    plt.xticks(future_years)  # 只显示整数年份

    # 在每个点上标注预测房价
    for i, price in enumerate(predict_prices):
        plt.text(future_years[i], price, str(price), ha='center', va='bottom')
    plt.grid(True)
    plt.tight_layout()


# 保存图片到指定路径
    save_path = f'{png_save_path}/未来{years}年房价预测趋势.png'
    plt.savefig(save_path)
    plt.close()
    print(f"未来{years}年房价预测趋势图已保存")

if __name__ == '__main__':
    # 设置源文件路径
    xlsx_path = "E:\\pythonProjects\\PythonProject\\hz_project\\data\\cleanData\\hz_ajk.xlsx"
    # 预处理后的数据保存路径
    preprocessed_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\preprocessed.xlsx"

    # 调用预处理函数
    # df = data_processing(xlsx_path)
    # 调用数据可视化分析函数
    # df = data_visualization(preprocessed_path)
    # 调用数据分析建模函数
    # df=data_analysis_model(preprocessed_path)

    # 预测未来5年房价
    years = 5
    # 加载标准化器
    scaler_pkl = joblib.load("E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\scaler.pkl")
    # 加载模型
    model_pkl = joblib.load("E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result\\model.pkl")
    # 保存结果路径
    png_save_path = "E:\\pythonProjects\\PythonProject\\hz_project\\dataAnalysis\\result"
    # 调用预测函数
    price_future_predict(scaler_pkl, model_pkl, preprocessed_path, years, png_save_path)
