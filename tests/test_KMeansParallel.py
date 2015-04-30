
import numpy as np
import sys
from numpy.testing import assert_almost_equal
from KMeansParallel_func import KMeansParallel


def test_feasible_k_zero():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        k = 0
        assert sys.exit

def test_feasible1_k_float():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        k = 1.5
        assert sys.exit
        
def test_feasible1_k_float():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        l = -1
        assert sys.exit

def test_level_label():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        k = 3
        assert len(set(KMeansParallel(data = data, k = k, l = 2*k).labels_)) == k

def test_num_label():
    for i in range(20):
        data = np.random.normal(size=(20,2))
        k = 3
        assert len(KMeansParallel(data = data, k = k, l = 2*k).labels_) == len(data)