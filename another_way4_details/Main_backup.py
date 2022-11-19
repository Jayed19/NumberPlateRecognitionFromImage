import cv2
import numpy as np
import imutils

img = cv2.imread('IMG_20221104_081626_9.jpg')

# For Resizing with CV2
from resize import resize
img=resize(img,20)

# For Making Gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Shapes", img)
#cv2.waitKey(0)

rectKern = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, rectKern)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)

squareKern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
light = cv2.morphologyEx(img, cv2.MORPH_CLOSE, squareKern)
light = cv2.threshold(light, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Light Regions", light)
cv2.waitKey(0)


gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F,
   dx=1, dy=0, ksize=-1)
gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = 255 * ((gradX - minVal) / (maxVal - minVal))
gradX = gradX.astype("uint8")
cv2.imshow("Scharr", gradX)
cv2.waitKey(0)


# blur the gradient representation, applying a closing
# operation, and threshold the image using Otsu's method
gradX = cv2.GaussianBlur(gradX, (5, 5), 0)
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKern)
thresh = cv2.threshold(gradX, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Grad Thresh", thresh)
cv2.waitKey(0)


thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
cv2.imshow("Grad Erode/Dilate", thresh)
cv2.waitKey(0)


thresh = cv2.bitwise_and(thresh, thresh, mask=light)
thresh = cv2.dilate(thresh, None, iterations=2)
thresh = cv2.erode(thresh, None, iterations=1)
cv2.imshow("Final", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
# return the list of contours
#print(cnts)


lpCnt = None
roi = None
# loop over the license plate candidate contours
for cnt in cnts:
    x1,y1 = cnt[0][0]
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    
    if len(approx) == 4:
      
        x, y, w, h = cv2.boundingRect(cnt)

        ratio = float(w)/h
        if ratio >= 1.9 and ratio <= 2.2:
            cv2.putText(thresh, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            img = cv2.drawContours(thresh, [cnt], -1, (0,255,0), 3)
            print(approx)
            print("------")
            i=i+1
            print(i)
            crop_img = thresh[y:y+h, x:x+w]
            print("width: "+str(w))
            print("Height: "+str(h))
            print("ratio: "+str(ratio))
            cv2.imshow("Rectangle img",crop_img)
            cv2.waitKey(0)
        else:
            pass

cv2.imshow("Shapes", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

