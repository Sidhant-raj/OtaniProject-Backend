# Image PreProcessing
import cv2 as cv
import pytesseract
from PIL import Image

Img = cv.imread("C:\\Users\\sidha\\Desktop\\Project\\Manuscript.jpg", 0)

Img = cv.resize(Img, (720, 900))
_, binary_image = cv.threshold(Img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

cv.imshow("Image 1", binary_image)

# Perform OCR on the preprocessed image
custom_config = r'--oem 3 --psm 6'  # Custom configuration options for Tesseract OCR
recognized_text = pytesseract.image_to_string(Image.fromarray(binary_image), config=custom_config)

print("Recognized Text:")
print(recognized_text)

if cv.waitKey(0) == 27:
    cv.destroyAllWindows()
