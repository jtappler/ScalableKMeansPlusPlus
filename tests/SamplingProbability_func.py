
#!/usr/bin/python
import numpy as np
from CostFunction_func import CostFunction

#sample probability function
def SamplingProbability(c, data, l):
    cost = CostFunction(c, data)
    return np.array([(min(np.sum((c-pts)**2,axis=1))) * l / cost for pts in data])