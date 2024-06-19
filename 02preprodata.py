import glob
import pandas as pd

#-----------------------------------------数据预处理----------------------------------------
#---------每个样本有多段时间数据，选择数据最长的那段作为全部样本
# 获取文件夹A下所有CSV文件的路径
file_paths = glob.glob('G:\\behaviorDetect\codenew\data\dataset/*.csv')

for file_path in file_paths:
    # 读取样本文件
    data = pd.read_csv(file_path)

    # 计算相邻Global_Time的差值
    time_diff = data['Global_Time'].diff()

    # 找到连续记录数据的起始索引和结束索引
    consecutive_start = 0
    consecutive_end = 0
    max_consecutive_count = 1
    current_consecutive_count = 1

    for i in range(1, len(time_diff)):
        if time_diff[i] == 100:
            current_consecutive_count += 1
        else:
            if current_consecutive_count > max_consecutive_count:
                max_consecutive_count = current_consecutive_count
                consecutive_start = i - current_consecutive_count
                consecutive_end = i - 1
            current_consecutive_count = 1

    if current_consecutive_count > max_consecutive_count:
        max_consecutive_count = current_consecutive_count
        consecutive_start = len(time_diff) - current_consecutive_count
        consecutive_end = len(time_diff) - 1

    # 选择连续记录数据的起始索引和结束索引，替换当前的全部数据
    if max_consecutive_count > 1:
        data = data.iloc[consecutive_start:consecutive_end + 1]
        data.reset_index(drop=True, inplace=True)
        data.to_csv(file_path, index=False)





# #---------检测速度是否有异常值  发生剧烈跳变时为异常
#
#
# # 获取文件夹A下所有CSV文件的路径
# file_paths = glob.glob('G:\\behaviorDetect\code\data\dataset/*.csv')
#
# for file_path in file_paths:
#     # 读取样本文件
#     data = pd.read_csv(file_path)
#
#     # 设置时间窗口大小
#     window_size = 4
#
#     # 检测异常数据
#     anomalies = []
#     for i in range(len(data)):
#         if data['v_Vel'][i] == 0:
#             if i >= window_size:
#                 window_data = data[['Global_X', 'Global_Y']].iloc[i - window_size:i]
#                 if ((window_data.diff() != 0).sum() == window_size * 2).all():
#                     anomalies.append(i)
#
#     if len(anomalies) > 0:
#         # 获取异常数据的Vehicle_ID和Global_Time
#         abnormal_vehicle_ids = data['Vehicle_ID'].iloc[anomalies]
#         abnormal_global_times = data['Global_Time'].iloc[anomalies]
#
#         # 打印异常数据的Vehicle_ID和Global_Time
#         print(f"异常数据发现！样本文件: {file_path}")
#         print("异常数据的Vehicle_ID:")
#         print(abnormal_vehicle_ids[0])
#         print("异常数据的Global_Time:")
#         print(abnormal_global_times[0])

