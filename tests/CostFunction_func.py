
#!/usr/bin/python
import numpy as np

##cost function
def CostFunction(c,data):
        return np.sum([min(np.sum((c-pts)**2,axis=1)) for pts in data]) 