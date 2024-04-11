import cv2 as cv

# reading images 

# img = cv.imread("photos/cat.jpg")
# cv.imshow("Cat" , img)
# cv.waitKey(0)

# reading videos

capture = cv.VideoCapture("videos/dog.mp4")

while True :
    isTrue , dog = capture.read()
    cv.imshow("Dog" , dog)
    if cv.waitKey(20) & 0xff == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()
    