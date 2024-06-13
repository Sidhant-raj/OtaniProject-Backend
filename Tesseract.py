import cv2 as cv
import pytesseract

Path = input("Enter Path : ")

Img = cv.imread(Path)

Str = pytesseract.image_to_string(Img)
print(Str)
