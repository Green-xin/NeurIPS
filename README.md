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



