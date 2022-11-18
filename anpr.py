from PIL import Image
import pytesseract
#pip install pytesseract
# You have to manually setup tesseract-ocr-w64-setup-v5.2.0.20220712.exe (download Link: https://github.com/UB-Mannheim/tesseract/wiki) in C:\Program Files\Tesseract-OCR\ 
# and then copy ben.traineddata file to C:\Program Files\Tesseract-OCR\tessdata
#In the PC, added Bangla(india) language to Windows
import cv2 
#pip install opencv-python



pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')

img = r"IMG_20221104_081224_8.jpg"
NP_img = cv2.imread(img)  

print(pytesseract.image_to_string(Image.open(img),lang="ben"))