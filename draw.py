import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3) , dtype="uint8")

# 1. Paint the image a certain color
# blank[:] = 0,255,0;
# cv.imshow("blank" , blank)

# # 2. draw a rectangle 
# cv.rectangle(blank , (0,0) , (blank.shape[1]// 2 , blank.shape[0]// 2) , (0,400,115) , thickness= -1)
# cv.imshow("Rectangle" , blank)

# # 3. draw a circle
# cv.circle(blank , (blank.shape[1]// 2 , blank.shape[0]// 2),40 , (0,0,255) , thickness=-1)
# cv.imshow("Circle" , blank)

# # 4. draw a line 
# cv.line(blank , (0,250) , (blank.shape[1] , blank.shape[0]// 2) , (255,255,255) , thickness= 4)
# cv.imshow("line" , blank)

# 5. Write a text
cv.putText(blank,"Hello World!" , (55,450) , cv.FONT_HERSHEY_SIMPLEX , 2 , (0,255,0) , 5 )
cv.imshow("Text" , blank)
cv.waitKey(0)
