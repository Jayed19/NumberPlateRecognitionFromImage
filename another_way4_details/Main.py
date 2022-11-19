import cv2
import numpy as np

img = cv2.imread('IMG_20221104_081626_9.jpg')

# For Resizing with CV2
from resize import resize
img=resize(img,20)

# For Making Gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Shapes", img)
#cv2.waitKey(0)

# For increase or decrease gray threshold 
ret,thresh = cv2.threshold(img,127,255,0)
cv2.imshow("Shapes", img)
cv2.waitKey(0)


#For Finding each small object like square or rectangle etc
contours,hierarchy = cv2.findContours(thresh, 1, 2)
print("Number of contours detected:", len(contours))



for cnt in contours:
   x1,y1 = cnt[0][0]
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   if len(approx) == 4:
      x, y, w, h = cv2.boundingRect(cnt)
      ratio = float(w)/h
      if ratio >= 0.9 and ratio <= 1.1:
         img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
         cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
      else:
         cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()