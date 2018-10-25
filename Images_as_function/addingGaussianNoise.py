import cv2
import numpy as np 

image1 = cv2.imread("images/gray_image2.png")

width, height = image1.shape[0], image1.shape[1] 

mean = 0 
var = 0
sigma = var**0.5

gauss = np.random.normal(mean, sigma, (width, height, 3))
gauss = gauss.reshape(width, height, 3)
new_image = image1 + gauss

cv2.imshow('normal image', image1)

cv2.imshow('noisy image',  new_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 