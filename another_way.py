import cv2
import pytesseract

image = cv2.imread('IMG_20221104_081224_8.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Blur and perform text extraction(you can use raw image)
thresh = cv2.GaussianBlur(thresh, (3,3), 0)
pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
data = pytesseract.image_to_string(thresh, lang='ben', config='--psm 6')
print(data)