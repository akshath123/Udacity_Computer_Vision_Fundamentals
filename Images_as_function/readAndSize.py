import cv2
import matplotlib.pyplot as plt 

img = cv2.imread("images/gan.png")

print(img.shape)

#plt.figure()
#plt.plot(img[50, :])
#plt.show()

# Cropping an image
#cv2.imshow('crop', img[20:100, 20:100])
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Taking only the red channel
red = img[:, :, 0]

cv2.imshow('red_channel', red)
cv2.waitKey(0)
cv2.destroyAllWindows() 

print( red.shape )