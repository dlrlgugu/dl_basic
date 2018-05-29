import numpy as np

x = np.random.randn(2,3)

def normalizeRows(x):
    n = np.linalg.norm(x,axis=1,keepdims=True)
    return x/n

print (normalizeRows(x))
