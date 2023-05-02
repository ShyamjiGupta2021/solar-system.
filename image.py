import cv2
import numpy

img=cv2.imread('solar-system.jpg')
cv2.putText(img,"Sun",(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Venus",(100,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Mercury",(150,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Earth",(280,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Mars",(370,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Jupiter",(500,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Saturn",(750,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Uranus",(950,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))
cv2.putText(img,"Neptune",(1100,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,255))

cv2.imshow('output',img)
cv2.waitKey(10000)
print(img)