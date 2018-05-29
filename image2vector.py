
import numpy as np

image = np.random.randn(3,3,2)

def image2vector(image):
    v=image.reshape(image.shape[0]*image.shape[1],image.shape[2])
    return v

print (image2vector(image).shape)
