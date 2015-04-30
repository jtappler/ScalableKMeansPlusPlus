
#!/usr/bin/python
from __future__ import division
import os
import sys
import glob
import random
import sklearn
import sklearn.cluster
import numpy as np
from CostFunction_func import CostFunction
from SamplingProbability_func import SamplingProbability


def KMeansParallel(data, k, l):
    N = data.__len__()
    if k <= 0 or not(isinstance(k,int)) or l <= 0:
        sys.exit("illegal input")    
    # Then we start to Implement the algorithm
    # 1. Sample one point uniformly at random from X
    c = np.array(data[np.random.choice(range(N),1),])
    # 2. To Cost function
    phi = CostFunction(c, data)
    # 3. Looping
    for i in range(np.ceil(np.log(phi)).astype(int)):
        cPrime = data[SamplingProbability(c,data,l) > np.random.uniform(size = N),]
        c = np.concatenate((c, cPrime))
    # End looping
    # 7. For x in C, set w_x to be the number of pts closest to X
    cMini = [np.argmin(np.sum((c-pts)**2,axis=1)) for pts in data];
    closerPts = [cMini.count(i) for i in range(len(c))]
    weight = closerPts/np.sum(closerPts)
    # 8. Recluster the weighted points in C into k clusters
    allC = data[np.random.choice(range(len(c)),size=1,p=weight),]
    data_final = c
    for i in range(k-1):
        Probability = SamplingProbability(allC,data_final,l) * weight
        # choose next centroid
        cPrimeFin = data[np.random.choice(range(len(c)), size=1, p=Probability/np.sum(Probability)),]
        allC = np.concatenate((allC,cPrimeFin))
    KMeansPP = sklearn.cluster.KMeans(n_clusters=k, n_init=1, init=allC, max_iter=500, tol=0.0001)
    KMeansPP.fit(data);
    return KMeansPP