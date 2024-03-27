import cv2
import numpy as np


image = cv2.imread('train_0001.jpg')  


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)


combined = np.sqrt(grad_x**2 + grad_y**2)
combined = np.uint8(np.absolute(combined))


cv2.imshow('Edge Detection', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
