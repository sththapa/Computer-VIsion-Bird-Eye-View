import cv2
import numpy as np

# print(kernel)
kernel = np.ones((5,5),np.uint8)
path = "santosh.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)
imgEorde = cv2.erode(imgDilation,kernel,iterations=2)
cv2.imshow("Santosh",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dialted",imgDilation)
cv2.imshow("Erode",imgEorde)

cv2.waitKey(0)







