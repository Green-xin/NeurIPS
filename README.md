# NeurIPS
Data Analysis


Trajectory data analysis

Vehicle trajectory data refers to the data that describes the path and state of the vehicle's movement, including the position, velocity, acceleration and other related motion parameters of the vehicle over a period of time. Vehicle trajectory data is typically collected and recorded through vehicle sensors or other traffic monitoring devices such as traffic cameras or radar. This section begins with a detailed explanation of NGSIM and then pre-processes the raw data of the NGSIM dataset. Vehicle trajectory data refers to the data that describes the path and state of the vehicle's movement, including the position, velocity, acceleration and other related motion parameters of the vehicle over a period of time. Vehicle trajectory data is typically collected and recorded through vehicle sensors or other traffic monitoring devices such as traffic cameras or radar. This section begins with a detailed explanation of NGSIM and then pre-processes the raw data of the NGSIM dataset.

Dataset Analysis

In this paper, aggressive driving behavior recognition is carried out using the NGSIM dataset, a large-scale traffic data collection project funded by the American Traffic Management Research Program. The dataset provides high-quality traffic trajectory data for use in areas such as traffic flow analysis, traffic simulation, and driving behavior research.
NGSIM datasets are collected by using video cameras and radar sensors. During the acquisition process, video cameras are used to record traffic scenes, capturing the vehicle's movement trajectory and behavior. At the same time, radar sensors are used to measure information such as the speed and position of vehicles. Together, these collection devices provide accurate and detailed traffic trajectory data. The data is presented in a CSV file, and the meanings of each field in the file are shown in Table 3.1.

Trajectory data preprocessing
The acquired NGSIM dataset was last updated on March 9, 2022, with more than 11.85 million samples and 24 fields. In the aggressive driving behavior, the main focus is on the speed and acceleration of the driving vehicle, so the vehicle identification number, timestamp, global abscissa and ordinate of the vehicle, instantaneous vehicle speed, instantaneous acceleration of the vehicle and highway name were selected as the experimental data.

The data collected vehicle information in four areas, and in order to ensure the consistency of the experimental data, only the data of the US-101 highway were selected for the experiment. In order to facilitate the collection of various information of the same vehicle, the data of the same vehicle is summarized into the same folder according to the vehicle identification number, which is used as a training sample for aggressive driving behavior recognition.
In the process of data collection, the vehicle may stop, resulting in the presence of multiple segments of driving data in the vehicle. The driver of the same vehicle will not change on the road, that is, the driver of the same vehicle has the same driving style, so the longest period of multi-segment driving is selected as the driving data of the current vehicle.
According to the above data preprocessing process, 3109 vehicle trajectory data samples are sorted out, taking a sample as an example, the vehicle speed and acceleration monitoring data are shown in Figure 1.

Figure 1
![2](https://github.com/Green-xin/NeurIPS/assets/173121166/a86dc76c-0cae-495e-89c9-018500d660a5)



Aggressive driving behavior feature extraction

In aggressive driving behavior recognition, feature extraction establishes the premise of aggressive driving behavior recognition model, and data feature extraction can help identify key information in aggressive driving behavior. By mining the relevant features in driving behavior, such as speed, acceleration, etc., it is possible to capture the characteristic patterns of aggressive driving. These characteristics can provide an important basis for driver behavior.

Data dimensionality reduction based on principal component analysis

After feature extraction, the obtained aggressive driving behavior features have redundant information and high correlation, which leads to the problem of overfitting, the increase of computational complexity and the decrease of the generalization ability of the model. Principal Component Analysis (PCA) can be used to map high-dimensional feature spaces to lower-dimensional subspaces, thereby reducing the number of features.
PCA is a commonly used data dimensionality reduction and feature extraction method that converts high-dimensional data into low-dimensional representations while retaining the most important information in the data. The goal of principal component analysis is to project the original data into a new coordinate system through a linear transformation, so as to maximize the variance of the data in the new coordinate system. In the new coordinate system, the first principal component explains the maximum variance in the original data, the second principal component explains the second largest variance, and so on. Reduce the dimension of the data from high to low dimensions by selecting the most important principal components.


The steps for PCA are as follows:
Step 1: Normalize the data: Normalize the raw data so that the mean value of each feature is 0 and the variance is 1 to eliminate the dimensional influence between different features.
Step 2: Calculate the covariance matrix of the normalized data, which describes the linear relationship between the features in the data.
Step 3: Decompose the eigenvalues of the covariance matrix to obtain the eigenvalues and corresponding eigenvectors. The eigenvector represents the direction of the new coordinate system, while the eigenvalues represent the magnitude of the variance of the data in those directions.
Step 4: According to the size of the eigenvalues, select the most important k eigenvectors as the principal components, where k is the target dimension to be reduced.
Step 5: Project the normalized raw data onto the selected principal components to obtain the reduced data.
PCA was used to reduce the dimensionality of aggressive driving behavior feature data, and the variance, contribution rate and cumulative contribution rate of each feature were obtained, as shown in Table 3.3.
From the cumulative contribution rate in Table 4.3, it can be seen that the cumulative contribution rate of PC1, PC2 and PC3 to the data reaches 87%, so PC1, PC2 and PC3 are used as the principal components of aggressive driving behavior recognition, that is, the input of the clustering model.


Aiming at the principal component features after dimensionality reduction, K-means clustering was used to identify aggressive driving behaviors. In this section, the number of clusters is determined by the elbow rule, then the principal components of the trajectory data are clustered by the K-means clustering method, and finally the contour coefficient is used to evaluate whether the clustering is reasonable.
In cluster analysis, the elbow rule is used to determine the best choice for the number of clusters. This method helps to determine a reasonable number of clusters by plotting the relationship between the number of clusters and the sum of squared errors (SSE) of the clustering model.


The idea of the elbow rule is that as the number of clusters increases, the value of SSE decreases gradually, because increasing the number of clusters better fits the training data. However, when the number of clusters increases to a certain extent, the improvement effect of each new cluster center on SSE gradually decreases. At this time, the improvement of SSE is no longer significant with the increase in the number of clusters, and the image presents an obvious "elbow" shape.
Figure 2 shows the elbow rule diagram calculated using principal component features, and it can be observed from the data in the figure that the degree of SSE changes significantly when the number of clusters k is less than 4. In the recognition of aggressive driving behavior, it is necessary to classify normal driving behavior and aggressive driving behavior, so the number of clusters is set to 2 to obtain the classification of aggressive and normal driving behavior.

Figure 2
![3](https://github.com/Green-xin/NeurIPS/assets/173121166/7b719d9e-eed0-4d7a-9cdf-21798c471692)







