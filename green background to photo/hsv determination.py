#determining hsv values from decimal colour codes
import cv2
import numpy

#uint8 is unsigned 8 bit integer of values 0-255 int on the otherhand is a 32 bit signed integer.
#Red =(255,0,0)
#lime=(0,255,0)
#yellow=(255,255,0)
#red=(0,0,255)

'''hsv is mostly used when we are selecting colours,It corresponds better to how people experience colour than rgb
It is used to separate image luminance from colour information.'''

green=numpy.uint8([[[255,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

print(hsv_green)

cv2.waitKey(0)

#Find the lower bound and upper bound of the colour using :
#lower=[h-10,100,100]
#upper=[h+10,255,255]
