import cv2
import matplotlib.pyplot as plt


img=cv2.imread('img1.jpg')
plt.imshow(img)
plt.show()
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img_rgb,cmap='gray')
plt.show()