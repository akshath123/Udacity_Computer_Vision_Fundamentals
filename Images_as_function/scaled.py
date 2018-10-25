import cv2
import numpy as np

image1 = cv2.imread('images/gray_image.jpg')

image_scaled = 0.001 * image1

cv2.imshow('scaled', image_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()