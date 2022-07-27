
import cv2
import numpy

video=cv2.VideoCapture("greeny.mp4")
image=cv2.imread("1-happiness.JPG")

while True:
    ret,frame=video.read()#If any error in loading the video the ret condition becomes false
    frame=cv2.resize(frame,(1200,700),)
    image=cv2.resize(image,(1200,700),)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue,saturation,volume

    l_g=numpy.array([32,94,132])#[]
    u_g=numpy.array([179,255,255])#[]
    mask=cv2.inRange(hsv,l_g,u_g)#The mask is created to cover the green values
    res=cv2.bitwise_and(frame,frame,mask=mask)
    #cv2.imshow("Frame",frame)#name of the video frame="Frame"
    #cv2.imshow("Mask",mask)
    #cv2.imshow("resultant",res)

    f=frame-res
    #print(f)
    f=numpy.where(f==0,image,f) #replace the places in the screen where f =black on other places f=f
    cv2.imshow("final",f)
    #cv2.imshow("prefinal",f)
    k=cv2.waitKey(1)#waitKey method waits for you to press a key and the unicode value of the key is saved in k
    if k==ord("q"):
        break
video.release()
cv2.destroyAllWindows()

