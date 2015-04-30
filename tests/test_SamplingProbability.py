
import numpy as np
from numpy.testing import assert_almost_equal
from SamplingProbability_func import SamplingProbability
from CostFunction_func import CostFunction

def test_positive_probability():
    l = 2
    for i in range(20):
        data = np.random.normal(size=(20,2))
        c = data[np.random.choice(range(20),1),]
        assert np.alltrue(SamplingProbability(c,data,l) >= 0)

def test_sum_to_l():
    for i in range(20):
        l = i + 1
        data = np.random.normal(size=(20,2))
        c = data[np.random.choice(range(20),1),]
        assert (np.sum(SamplingProbability(c,data,l)) - l) <= 1e-6

def test_zero_probability():
    l = 2
    for i in range(20):
        data = np.random.normal(size=(20,2))
        choice = np.random.choice(range(20),1)
        c = data[choice,]
        Probability = SamplingProbability(c,data,l)
        assert np.alltrue(Probability[choice,] == 0)