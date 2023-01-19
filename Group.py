#Face Detection
import cv2

img = cv2.imread('//home//rajesh//Desktop//week1//Task 2//pics//111.jpg')
model = cv2.CascadeClassifier(r"//home//rajesh//Desktop//week1//Task 2//haarcascade_frontalface_default.xml")
# This haarcascade_frontalface_default.xml file downloaded from web
     
face = model.detectMultiScale(img)
for x,y,width,height in face:
    cv2.rectangle(img,(x,y),(x+width,y+width),(64,64,255),5)    #top left (x,y), bottom right (x+width,y+width), colour code according to BGR, thickness of rectangle
    cv2.imshow("IMAGE",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()