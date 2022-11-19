import cv2
import numpy as np

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray)
cv2.waitKey(0)

#ret,thresh = cv2.threshold(gray,50,255,0)
ret,thresh = cv2.threshold(gray,127,255,0)
#Here ret is the threashold value and thresh is the threshold Image
cv2.imshow("Thresh Image",thresh)
print(ret) # threshold change kore kore dekhte hobe
cv2.waitKey(0)



contours,hierarchy = cv2.findContours(thresh, 1, 2)

print("total Number of contours detected:", len(contours))

i=0
for cnt in contours:
   x1,y1 = cnt[0][0]
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   
   if len(approx) == 4:
      
      x, y, w, h = cv2.boundingRect(cnt)
      ratio = float(w)/h
      if ratio >= 0.9 and ratio <= 1.1:
        pass
         #img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
         #cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
         #print(approx)
         #print("------")
      else:
         cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
         print(approx)
         print("------")
         i=i+1
         print(i)
         crop_img = img[y:y+h, x:x+w]
         print("width: "+str(w))
         print("Height: "+str(h))
         cv2.imshow("Rectangle img",crop_img)
         cv2.waitKey(0)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()