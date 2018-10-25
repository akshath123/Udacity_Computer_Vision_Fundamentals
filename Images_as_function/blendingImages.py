import cv2
import numpy as np 

def blendImages(img1, img2, alpha):
	return ((img1 * alpha) + (img2 * (alpha - 1)))

img1 = cv2.imread('images/gray_image.jpg')
img1 = cv2.resize(img1, (150, 200))
img2 = cv2.imread('images/gray_image2.png')

cv2.imshow('gray', blendImages(img1, img2, 0.)5)
cv2.waitKey(0)
cv2.destroyAllWindows()