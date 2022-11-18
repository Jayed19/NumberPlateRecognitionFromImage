import cv2
import pytesseract

image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("input",gray)
if cv2.waitKey(0) & 0xff == ord('q'):
    pass
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow("input",thresh)
if cv2.waitKey(0) & 0xff == ord('q'):
    pass
# Blur and perform text extraction(you can use raw image)
thresh = cv2.GaussianBlur(thresh, (3,3), 0)
cv2.imshow("input",thresh)
if cv2.waitKey(0) & 0xff == ord('q'):
    pass
pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
data = pytesseract.image_to_string(thresh, lang='ben', config='--psm 6')
print(data)