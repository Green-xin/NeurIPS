import glob
import os

import pandas as pd

#-----------------------------------------特征提取----------------------------------------
# Vehicle_ID：样本ID
# avgX_Vel：横向速度平均值
# stdX_Vel：横向速度标准差
# medianX_Vel：横向速度中位数
# avgX_Acc：横向加速度平均值
# stdX_Acc：横向加速度标准差
# medianX_Acc：横向加速度中位数
# avgY_Vel：纵向速度平均值
# stdY_Vel：纵向速度标准差
# medianY_Vel：纵向速度中位数
# avgY_Acc：纵向加速度平均值
# stdY_Acc：纵向加速度标准差
# medianY_Acc：纵向加速度中位数
# Space_Headway:车头间距



# 文件夹A的路径
folder_path = r'G:\behaviorDetect\codenew\data\dataset'  # 请替换为实际的文件夹路径

# 读取文件夹A下的所有CSV文件
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 存储每个车辆的特征的列表
features_list = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    # 剔除v_Vel值为20以下的数据
    df = df[df['v_Vel'] > 20]

    # 利用五点求导法计算纵向速度和纵向加速度
    df['Y_Vel'] = -df['Global_Y'].diff(2) / df['Global_Time'].diff(2)  * 1000
    df['Y_Acc'] = -df['Y_Vel'].diff(2) / df['Global_Time'].diff(2)  * 1000

    # 利用五点求导法计算横向速度和横向加速度
    df['X_Vel'] = df['Global_X'].diff(2) / df['Global_Time'].diff(2)  * 1000
    df['X_Acc'] = df['X_Vel'].diff(2) / df['Global_Time'].diff(2) * 1000

    # 提取特征
    features = {
        'avgX_Vel': df['X_Vel'].mean(),
        'stdX_Vel': df['X_Vel'].std(),
        'medianX_Vel': df['X_Vel'].median(),
        'avgX_Acc': df['X_Acc'].mean(),
        'stdX_Acc': df['X_Acc'].std(),
        'medianX_Acc': df['X_Acc'].median(),
        'avgY_Vel': df['Y_Vel'].mean(),
        'stdY_Vel': df['Y_Vel'].std(),
        'medianY_Vel': df['Y_Vel'].median(),
        'avgY_Acc': df['Y_Acc'].mean(),
        'stdY_Acc': df['Y_Acc'].std(),
        'medianY_Acc': df['Y_Acc'].median(),
        'Space_Headway': df['Space_Headway'].std()  # 假设所有车辆的车头间距相同，取第一个值
    }

    # 将特征添加到列表中
    features_list.append(features)

# 创建包含所有样本特征的数据框datanew
datanew = pd.DataFrame(features_list)

# 保存datanew到指定路径下的CSV文件
datanew.to_csv(r'G:\behaviorDetect\codenew\data\features.csv', index=False)  # 请替换为实际的保存路径
