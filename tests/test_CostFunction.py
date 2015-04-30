
import numpy as np
from numpy.testing import assert_almost_equal
from CostFunction_func import CostFunction

def test_postive_cost():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        c = data[np.random.choice(range(20),1),]
        assert CostFunction(c, data) >= 0

def test_c_equals_data():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        c = data
        assert CostFunction(c, data) == 0

def test_larger_c_smaller_cost():
     for i in range(20):
        data = np.random.normal(size=(20,2))
        larger_c = data[np.random.choice(range(20),5,replace=False),]
        c = larger_c[:4,]
        assert CostFunction(larger_c, data) <= CostFunction(c, data)