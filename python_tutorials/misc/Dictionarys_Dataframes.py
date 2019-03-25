import numpy as np 
import subprocess as sh 
import pandas as pd

Total_timeframes=2
Discs = 23
radius_ext = 8.45E-9
radius_cont = 1.13E-8
midpoint = (radius_ext + radius_cont)/2 


Times = ['T_{}'.format(i) for i in range(Total_timeframes)]
Elastic_Rod_Data= {}
for i,time in enumerate(Times):
    Elastic_Rod_Data[time] = pd.read_csv('SheathH_R_{}.csv'.format(i), delimiter = ',', header=None)

radius_data = np.zeros([115,Total_timeframes])
for i,key in enumerate(Elastic_Rod_Data):
    radius_data[:,i] = Elastic_Rod_Data[key].iloc[:,1]
