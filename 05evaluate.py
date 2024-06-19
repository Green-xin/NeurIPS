import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

#-----------------------------------------评估模型----------------------------------------
# 打印聚类结果
data_normalized_df = pd.read_csv(r"F:\20240611数据建模\codenew\codenew\data\infer.csv")
data_normalized_df = data_normalized_df.drop("Unnamed: 0", axis=1)
labels = data_normalized_df['cluster_label']
# 统计 cluster_label 的值计数
label_counts = labels.value_counts()

# 获取 cluster_label 为 0 和 1 的样本数量
label_0_count = label_counts[0]
label_1_count = label_counts[1]

print("cluster_label为0的样本数量：", label_0_count)
print("cluster_label为1的样本数量：", label_1_count)
# # 提取要可视化的字段和聚类标签
# --------------肘部法则
data_normalized_df.columns = data_normalized_df.columns.astype(str)

# 初始化空列表存储每个聚类数量的误差平方和
sse = []
# 设置聚类数量的范围（假设从2到10）
k_range = range(2, 11)

# 计算每个聚类数量对应的误差平方和
for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init=5)
    kmeans.fit(data_normalized_df)
    sse.append(kmeans.inertia_)

# 绘制肘部法则曲线
plt.plot(k_range, sse, 'bo-')
plt.xlabel('聚类数量')
plt.ylabel('误差平方和')
plt.title('肘部法则')
# plt.savefig('G:\\behaviorDetect\codenew\\fig\肘部法则聚类数量误差平方和.svg', format='svg')
plt.show()

# --------------轮廓系数
from sklearn.metrics import silhouette_score
# 计算轮廓系数
silhouette_avg = silhouette_score(data_normalized_df, labels)

print("聚类模型的轮廓系数: ", silhouette_avg)






# 创建3D图形
# 计算最后一列标签的均值和标准差
label_mean = labels.mean()
label_std = labels.std()
# 指定阈值，例如标准差的3倍
threshold = 2 * label_std
# 根据阈值筛选离群点
outliers = np.abs(labels - label_mean) > threshold
# 去除离群点
data_filtered = data_normalized_df.loc[~outliers]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 根据聚类标签绘制不同颜色的数据点
scatter = ax.scatter(data_filtered['0'], data_filtered['1'], data_filtered['2'], c=labels, cmap='viridis')

# 设置坐标轴标签
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

# 添加颜色图例
legend = ax.legend(*scatter.legend_elements(), title='Clusters')
ax.add_artist(legend)

# 显示图形
plt.show()


#计算每类特征均值
# 读取包含数据的DataFrame
# 按照'cluster_label'列进行分组，并计算每个类别的特征均值
alldata = pd.read_csv('G:\\behaviorDetect\codenew\data\\features.csv',usecols=lambda column: column != 'Vehicle_ID',index_col=None)
# alldata = alldata.drop("Unnamed: 0", axis=1)
data_cleaned = alldata[~alldata.isin([np.inf, -np.inf, np.nan]).any(axis=1)]
data_cleaned = data_cleaned.reset_index(drop=True)
data_cleaned['cluster_label'] = labels

mean_features = data_cleaned.groupby('cluster_label').mean()

# 保存特征均值到CSV文件
mean_features.to_csv('G:\\behaviorDetect\codenew\data\cluster_mean_features.csv', index=False)