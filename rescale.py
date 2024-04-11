import cv2 as cv

def rescaleFrame(frame , scale = .75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width , height);
    
    return cv.resize (frame , dimensions , interpolation= cv.INTER_AREA)
    
# capture = cv.VideoCapture('videos/dog.mp4')

# while True :
#     isTrue , frame = capture.read()
#     frame_resized = rescaleFrame(frame)
    
#     # cv.imshow( "Video", frame);
#     # cv.imshow("Video Resized" , frame_resized);
    
#     if cv.waitKey(20) & 0xff == ord('q'):
#         break;

# capture.release();
# cv.destroyAllWindows();

#  resizing image

img = cv.imread('photos/cat.jpg')
resize_image = rescaleFrame(img,scale=2);

cv.imshow('Cat' , img)
cv.imshow("resized image" , resize_image)
cv.waitKey(0)