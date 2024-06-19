import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler


#-----------------------------------------数据降维----------------------------------------
# --------------------主成分分析
# # 读取特征数据的DataFrame
features_df = pd.read_csv(r'F:\20240611数据建模\codenew\codenew\data\features.csv')  # 用实际的特征数据文件路径替换'your_data.csv'

# 提取要进行因子分析的特征列
features = ['avgX_Vel', 'stdX_Vel', 'medianX_Vel',
            'avgX_Acc', 'stdX_Acc', 'medianX_Acc',
            'avgY_Vel', 'stdY_Vel', 'medianY_Vel',
            'avgY_Acc', 'stdY_Acc', 'medianY_Acc',
            'Space_Headway']
data = features_df[features]
# 剔除包含无穷大和缺失值的样本
data_cleaned = data[~data.isin([np.inf, -np.inf, np.nan]).any(axis=1)]
# 重置索引
data_cleaned = data_cleaned.reset_index(drop=True)
# 归一化数据
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data_cleaned)
# 转换为DataFrame
data_normalized_df = pd.DataFrame(data_normalized, columns=features)


import numpy as np
from sklearn.decomposition import PCA

data_array = data_normalized_df.values
pca = PCA()
pca.fit(data_array)
eigenvalues = pca.explained_variance_
variance_ratio = pca.explained_variance_ratio_
cumulative_variance_ratio = np.cumsum(variance_ratio)
print(eigenvalues)
print(variance_ratio)
print(cumulative_variance_ratio)


principal_components = pca.transform(data_array)
principal_components_3 = principal_components[:, :3]
principal_components_df = pd.DataFrame(principal_components_3, columns=['PC1', 'PC2', 'PC3'])
principal_components_df.to_csv("G:\\behaviorDetect\codenew\data\\principal_components.csv")

# -----------------------------------------训练模型----------------------------------------
# 读取包含样本数据的CSV文件
features = pd.read_csv('G:\\behaviorDetect\codenew\data\\principal_components.csv')
features = features.drop("Unnamed: 0", axis=1)
# 剔除包含无穷大和缺失值的样本
data_cleaned = features[~features.isin([np.inf, -np.inf, np.nan]).any(axis=1)]

# 重置索引
data_cleaned = data_cleaned.reset_index(drop=True)

# 归一化数据
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data_cleaned)

data_normalized_df = pd.DataFrame(data_normalized)


# 创建KMeans聚类模型
kmeans = KMeans(n_clusters=2,n_init=5)  # 假设聚类为3个簇

# 执行聚类
kmeans.fit(data_normalized_df)

# 获取每个样本的聚类标签
labels = kmeans.labels_

# 将聚类标签添加到原始数据中
data_normalized_df['cluster_label'] = labels

data_normalized_df.to_csv("G:\\behaviorDetect\codenew\data\infer.csv")