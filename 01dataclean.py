import pandas as pd

#-----------------------------------------数据清理----------------------------------------
# 读取CSV文件
data = pd.read_csv('G:\\behaviorDetect\codenew\data\\Next_Generation_Simulation__NGSIM__Vehicle_Trajectories_and_Supporting_Data_20240407.csv')

# 筛选Location为"us-101"的数据
filtered_data = data[data['Location'] == 'us-101']

# 选择需要保存的字段
selected_fields = ['Vehicle_ID', 'Global_Time', 'Global_X', 'Global_Y', 'v_Vel', 'v_Acc', 'Space_Headway']

# 保存简化后的数据到新CSV文件
filtered_data[selected_fields].to_csv('G:\\behaviorDetect\codenew\data\data.csv', index=False)

#-----------------------------------------数据集建立----------------------------------------
# 读取清理后的CSV文件
data = pd.read_csv('G:\\behaviorDetect\codenew\data\data.csv')

# 按照Vehicle_ID分组，并按照Global_Time排序
data = data.sort_values(['Vehicle_ID', 'Global_Time'])

# 将每个分组保存到不同的CSV文件中
output_folder = 'G:\\behaviorDetect\codenew\data\dataset'  # 文件夹A的路径

for vehicle_id, group in data.groupby('Vehicle_ID', as_index=False):
    output_file_path = output_folder + f'vehicle_{vehicle_id}.csv'
    group.to_csv(output_file_path, index=False)




