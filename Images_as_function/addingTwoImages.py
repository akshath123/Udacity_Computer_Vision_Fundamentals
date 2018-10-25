import cv2
import numpy as np  

image1 = cv2.imread('images/gray_image.jpg')
image2 = cv2.imread('images/gray_image2.png')

image1 = cv2.resize(image1, (150, 200))

print("Image 1 shape ", image1.shape)
print("Image 2 shape ", image2.shape)

# Added Images using numpy array
image3 = image1 + image2 
cv2.imshow("Numpy array", image3)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# Adding using Open CV
image4 = cv2.add(image2, image1)
cv2.imshow("Using CV", image4)
cv2.waitKey(0)
cv2.destroyAllWindows()