import cv2
import numpy as np
img = cv2.imread("deck.jpg")
width,height = 250,350
pst1 = np.array([[334,308],[619,80],[656,720],[949,492]],np.float32)
pst2 = np.array([[0,0],[width,0],[0,height],[width,height]],np.float32)
matrix = cv2.getPerspectiveTransform(pst1,pst2)
imageOutput = cv2.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    cv2.circle(img,(pst1[x][0],pst1[x][1]),5,(5,180,255),cv2.FILLED)

cv2.imshow("Original Image",img)
cv2.imshow("Output Image",imageOutput)
cv2.waitKey(0)