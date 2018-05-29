import numpy as np
import math

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

print (sigmoid(3))

x = np.array([1,2,3])
print (sigmoid(x))
