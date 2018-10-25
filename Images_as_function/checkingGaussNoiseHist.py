import cv2
import matplotlib.pyplot as plt 
import numpy as np 

noise = np.random.normal( size = 100)

plt.hist(noise, bins = [-3, -2, -1, 0, 1, 2, 3])
plt.xlabel('bins')
plt.ylabel('count')
plt.show()