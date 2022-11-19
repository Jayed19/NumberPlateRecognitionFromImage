import cv2
import numpy as np
import imutils

image=cv2.imread("IMG_20221104_081626_9.jpg")
image=imutils.resize(image,width=500)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
smooth_gray=cv2.bilateralFilter(gray,11,17,17)
edge=cv2.Canny=cv2.Canny(gray,170,200)

green_border_img=image.copy()
cnts,new=cv2.findContours(edge.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(green_border_img,cnts,-1,(0,255,0),3)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:100]

image2=image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)

count=0
name=1
for cnt in cnts:
    perimeter=cv2.arcLength(cnt,True)
    approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)

    if (len(approx==4)):
        NumberPlateCount=approx
        x,y,w,h=cv2.boundingRect(cnt)
        crop_img=image[y:y+h,x:x+w]
        cv2.imwrite(str(name)+'.jpg',crop_img)
        name +=1
        break

cv2.drawContours(image,[NumberPlateCount],-1,(0,255,0),3)

crop_image_final="1.jpg"
cv2.imshow("Final Croped",cv2.imread(crop_image_final))

cv2.imshow("Original Image",image)
cv2.imshow("Gray Image",gray)
cv2.imshow("Gray Smooth",smooth_gray)
cv2.imshow("Canny Image",edge)
cv2.imshow("Green Border",green_border_img)
cv2.imshow("Image2",image2)
cv2.waitKey(0)