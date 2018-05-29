import numpy as np

def loss1(yhat,y):
    loss = np.sum(np.absolute(y-yhat))
    return loss

def loss2(yhat,y):
    loss = np.power(y-yhat,2)
    loss = np.sum(loss)
    return loss

yhat = np.random.randn(1,5)
y = np.array([1,0,0,1,0])

print(loss2(yhat,y))
