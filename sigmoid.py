import numpy as np
import math

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

x = np.array([1,2,3])
print (sigmoid(x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s*(1-s)
    return ds

print (sigmoid_derivative(x))
