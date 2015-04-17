# Simulated "Real" Data Set
#!/usr/bin/python
import os
import sys
import glob
import numpy as np

def DataSimulation(n):
    mean0 = [0, 2]
    cov0 = [[1, 0.33], [0.33, 1]]
    data0 = np.random.multivariate_normal(mean0, cov0, n)
    data0 = np.hstack((data0, np.ones((data0.shape[0],1))))

    mean1 = [5, 7]
    cov1 = [[1, 0.33], [0.33, 1]]
    data1 = np.random.multivariate_normal(mean1, cov1, n)
    data1 = np.hstack((data1, np.ones((data1.shape[0],1)) * 2))

    mean2 = [10, 12]
    cov2 = [[1, 0.33], [0.33, 1]]
    data2 = np.random.multivariate_normal(mean2, cov2, n)
    data2 = np.hstack((data2, np.ones((data2.shape[0],1)) * 3))
    
    mean3 = [15, 17]
    cov3 = [[1, 0.33], [0.33, 1]]
    data3 = np.random.multivariate_normal(mean3, cov3, n)
    data3 = np.hstack((data3, np.ones((data2.shape[0],1)) * 4))

    data = np.vstack((data0, data1, data2, data3))
    np.random.shuffle(data)
    print (data.shape)
    return data

DataSimulation(50)